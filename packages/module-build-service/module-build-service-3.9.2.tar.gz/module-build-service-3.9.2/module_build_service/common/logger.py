# -*- coding: utf-8 -*-
# SPDX-License-Identifier: MIT
"""
Logging functions.

At the beginning of the MBS flow, init_logging(conf) must be called.

After that, logging from any module is possible using Python's "logging"
module as showed at
<https://docs.python.org/3/howto/logging.html#logging-basic-tutorial>.

Examples:

import logging

logging.debug("Phasers are set to stun.")
logging.info("%s tried to build something", username)
logging.warning("%s failed to build", task_id)

"""

from __future__ import absolute_import, print_function
import os
import logging
import logging.handlers
import inspect
import re
import signal
import sys

levels = {
    "debug": logging.DEBUG,
    "error": logging.ERROR,
    "warning": logging.WARNING,
    "info": logging.INFO,
}

level_flags = {
    "debug": levels["debug"],
    "verbose": levels["info"],
    "quiet": levels["error"],
}


log_format = "%(asctime)s - %(threadName)s - %(name)s - %(levelname)s - %(message)s"


class ModuleBuildFileHandler(logging.FileHandler):
    """
    FileHandler subclass which handles only messages generated during
    particular module build with `build_id` set in its constructor.
    """

    def __init__(self, build_id, filename, mode="a", encoding=None, delay=0):
        logging.FileHandler.__init__(self, filename, mode, encoding, delay)
        self.build_id = build_id

    def emit(self, record):
        # Imported here because of importing cycle between __init__.py,
        # scheduler and models.
        from module_build_service.scheduler.consumer import MBSConsumer

        # Check the currently handled module build and emit the message only
        # if it's associated with current module.
        build_id = MBSConsumer.current_module_build_id
        if not build_id or build_id != self.build_id:
            return

        logging.FileHandler.emit(self, record)


def _is_solv_object(o):
    """
    Returns true if the object is a libsolv object or contains one.
    (Contains is implemented pragmatically and might need to be extended)
    """
    if isinstance(o, (tuple, list)):
        return any(_is_solv_object(x) for x in o)
    else:
        return str(type(o)).startswith("<class 'solv.")


class _ReprString(str):
    """
    String that doesn't add quotes for repr()
    """
    def __repr__(self):
        return self


class ModuleBuildInitialHandler(logging.handlers.MemoryHandler):
    """
    MemoryHandler subclass that never flushes - we use this to record initial log
    messages for a Mock build so that we can write them into the build logs for
    the module or modules.
    """
    def __init__(self):
        logging.handlers.MemoryHandler.__init__(self, 0, flushOnClose=False)

    def handle(self, record):
        # Python libsolv proxies don't actually reference the underlying object
        # and keep it from being destroyed, so we need to avoid saving them
        # in record.args
        if any(_is_solv_object(a) for a in record.args):
            record.args = tuple(_ReprString(a) if _is_solv_object(a) else a for a in record.args)

        logging.handlers.MemoryHandler.handle(self, record)

    def shouldFlush(self, record):
        return False


class ModuleBuildLogs(object):
    """
    Manages ModuleBuildFileHandler logging handlers.
    """

    def __init__(self, build_logs_dir, build_logs_name_format, level=logging.INFO):
        """
        Creates new ModuleBuildLogs instance. Module build logs are stored
        to `build_logs_dir` directory.
        """
        self.initial_handler = None
        self.initial_logs = []
        self.handlers = {}
        self.build_logs_dir = build_logs_dir
        self.build_logs_name_format = build_logs_name_format
        self.level = level

    def path(self, db_session, build):
        """
        Returns the full path to build log of module with id `build_id`.
        """
        path = os.path.join(self.build_logs_dir, self.name(db_session, build))
        return path

    def name(self, db_session, build):
        """
        Returns the filename for a module build
        """
        name = self.build_logs_name_format.format(**build.json(db_session))
        return name

    def buffer_initially(self):
        """
        Starts saving messages before builds start - these messages will be
        added to all build logs
        """
        handler = ModuleBuildInitialHandler()
        handler.setLevel(self.level)

        log = logging.getLogger()
        log.setLevel(self.level)
        log.addHandler(handler)

        self.initial_handler = handler

    def start(self, db_session, build):
        """
        Starts logging build log for module with `build_id` id.
        """
        if not self.build_logs_dir:
            return

        log = logging.getLogger()

        # We've finished recording the initial setup logs that we replay
        # to all the build logs.
        if self.initial_handler:
            log = logging.getLogger()
            self.initial_logs = self.initial_handler.buffer
            log.removeHandler(self.initial_handler)
            self.initial_handler = None

        if build.id in self.handlers:
            return

        # Create and add ModuleBuildFileHandler.
        handler = ModuleBuildFileHandler(build.id, self.path(db_session, build))
        handler.setLevel(self.level)
        handler.setFormatter(logging.Formatter(log_format, None))
        log.setLevel(self.level)
        log.addHandler(handler)

        # Replay the initial logs to this handler
        for record in self.initial_logs:
            handler.handle(record)

        self.handlers[build.id] = handler

    def stop(self, build):
        """
        Stops logging build log for module with `build_id` id. It does *not*
        remove the build log from fs.
        """
        if build.id not in self.handlers:
            return

        handler = self.handlers[build.id]
        handler.flush()
        handler.close()

        # Remove the log handler.
        log = logging.getLogger()
        log.removeHandler(handler)
        del self.handlers[build.id]

    @property
    def current_log_stream(self):
        # Imported here because of importing cycle between __init__.py,
        # scheduler and models.
        from module_build_service.scheduler.consumer import MBSConsumer

        if MBSConsumer.current_module_build_id:
            handler = self.handlers.get(MBSConsumer.current_module_build_id)
            if handler:
                return handler.stream
            else:
                return sys.stderr
        else:
            return sys.stderr


class LocalRepo(object):
    def __init__(self, koji_tag):
        self.koji_tag = koji_tag
        self.current_downloads = set()
        self.total_downloads = 0
        self.completed_downloads = 0
        self.status = ""

    def start_downloads(self, total):
        self.status = "Downloading packages"
        self.total_downloads = total

    def start_download(self, url):
        self.current_downloads.add(url)

    def done_download(self, url):
        self.current_downloads.remove(url)
        self.completed_downloads += 1

    def show_status(self, stream, style):
        if self.total_downloads > 0:
            count = " {}/{}".format(self.completed_downloads, self.total_downloads)
        else:
            count = ""

        print("{}: {}{}".format(style(self.koji_tag, bold=True), self.status, count),
              file=stream)
        for url in self.current_downloads:
            print("    {}".format(os.path.basename(url)), file=stream)


# Used to split aaa\nbbbb\n to ('aaa', '\n', 'bbb', '\n')
NL_DELIMITER = re.compile('(\n)')
# Matches *common* ANSI control sequences
# https://en.wikipedia.org/wiki/ANSI_escape_code#CSI_sequences
CSI_SEQUENCE = re.compile('\033[0-9;]*[A-Za-z]')


class EraseableStream(object):
    """
    Wrapper around a terminal stream for writing output that can be
    erased.
    """

    def __init__(self, target):
        self.target = target
        self.lines_written = 0
        # We assume that the EraseableStream starts writing at column 0
        self.column = 0
        self.resize()

    def resize(self):
        self.size = os.get_terminal_size(self.target.fileno())

    def write(self, string):
        # We want to track how many lines we've written so that we can
        # back up and erase them. Tricky thing is handling wrapping.

        # Strip control sequences
        plain = CSI_SEQUENCE.sub('', string)

        for piece in NL_DELIMITER.split(plain):
            if piece == '\n':
                self.column = 0
                self.lines_written += 1
            else:
                self.column = self.column + len(piece)
                # self.column == self.size.column doesn't wrap -
                # normal modern terminals wrap when a character is written
                # that would be off-screen, not immediately when the
                # line is full.
                while self.column > self.size.columns:
                    self.column -= self.size.columns
                    self.lines_written += 1

        self.target.write(string)

    def erase(self):
        if self.column > 0:
            # move cursor to the beginning of line and delete whole line
            self.target.write("\033[0G\033[2K")
        for i in range(0, self.lines_written):
            # move up cursor and delete whole line
            self.target.write("\033[1A\033[2K")

        self.lines_written = 0
        self.column = 0


FG_COLORS = {
    'green': '32',
    'red': '91',
}


class MBSConsoleHandler(logging.Handler):
    """
    Special logging.Handler that is responsible for creating attractive and
    informative output when running a local build. To allow certain log
    messages to be handled differently for console output, methods in this
    class decorated with the @console_message decorator are propagated to
    the MBSLogger class.

    When MBSLogger method is called, a normal log record is generated using
    the format string from the decoration. The record is logged normally
    in the build log or to a non-console handler, but when the event is
    received by this handler, the original decorated method is called instead.
    This method can optionally return a new string to be output to the log,
    or simply update internal state without logging anything.

    This handler also implements the behavior that when the handler level
    is at its default INFO state, INFO level log messages are only shown if
    they have an extra 'console' attribute added by calling MBSLogger.console()
    rather than MBSLogger.info(). This allow further trimming down the
    set of messages logged to the console without losing the distinction between
    DEBUG and INFO.
    """
    console_messages = {}

    def __init__(self, *args, stream=sys.stderr, **kwargs):
        self.stream = stream

        self.tty = self.stream.isatty()
        if self.tty:
            self.status_stream = EraseableStream(self.stream)
        else:
            self.status_stream = None

        self.long_running = None
        self.repos = {}

        self.debug_formatter = logging.Formatter(log_format)
        self.info_formatter = logging.Formatter("%(message)s")
        self.error_formatter = logging.Formatter(
            self.style("%(levelname)s", bold=True, fg='red') + " - %(message)s")

        logging.Handler.__init__(self, *args, level=logging.INFO, **kwargs)

    def style(self, text, bold=False, fg=None):
        if self.tty:
            start = ""
            if bold:
                start += "\033[1m"
            if fg:
                start += "\033[" + FG_COLORS[fg] + "m"
            return start + text + "\033[0m"
        else:
            return text

    def emit(self, record):
        if self.level == logging.INFO and record.levelno == logging.INFO:
            if not getattr(record, 'console', False):
                return

        self.acquire()
        try:
            if self.tty:
                self.status_stream.erase()

            console_message_callback = self.console_messages.get(record.msg)
            if console_message_callback:
                formatted = console_message_callback(self, *record.args)
            else:
                if self.level < logging.INFO:
                    formatted = self.debug_formatter.format(record)
                elif record.levelno == logging.INFO:
                    formatted = self.info_formatter.format(record)
                else:
                    formatted = self.error_formatter.format(record)

            if formatted:
                if self.long_running:
                    print(file=self.stream)
                    self.long_running = None

                print(formatted, file=self.stream)

            if self.tty:
                if self.repos:
                    print('------------------------------', file=self.status_stream)
                for repo in self.repos.values():
                    repo.show_status(self.status_stream, self.style)
        finally:
            self.release()

    def console_message(msg):
        def decorate(f):
            f.console_message = msg
            return f

        return decorate

    def resize(self):
        if self.status_stream:
            self.status_stream.resize()

    @console_message("%s ...")
    def long_running_start(self, msg):
        if self.long_running:
            print("", file=self.stream)
        self.long_running = msg
        print("{} ...".format(msg),
              file=self.stream, end="")
        self.stream.flush()

    @console_message("%s ... done")
    def long_running_end(self, msg):
        if self.long_running == msg:
            self.long_running = None
            print(" done",
                  file=self.stream)
        else:
            self.long_running = None
            return "{} ... done".format(msg)

    @console_message("%s: Making local repository for Koji tag")
    def local_repo_start(self, koji_tag):
        repo = LocalRepo(koji_tag)
        self.repos[koji_tag] = repo

        return "{}: Making local repository for Koji tag".format(
            self.style(koji_tag, bold=True))

    @console_message("%s: %s")
    def local_repo_done(self, koji_tag, message):
        del self.repos[koji_tag]

        return "{}: {}".format(
            self.style(koji_tag, bold=True),
            self.style(message, fg='green', bold=True))

    @console_message("%s: Downloading %d packages from Koji tag to %s")
    def local_repo_start_downloads(self, koji_tag, num_packages, repo_dir):
        repo = self.repos[koji_tag]
        repo.start_downloads(num_packages)

    @console_message("%s: Downloading %s")
    def local_repo_start_download(self, koji_tag, url):
        repo = self.repos[koji_tag]
        repo.start_download(url)

    @console_message("%s: Done downloading %s")
    def local_repo_done_download(self, koji_tag, url):
        repo = self.repos[koji_tag]
        repo.done_download(url)

    @classmethod
    def _setup_console_messages(cls):
        for value in cls.__dict__.values():
            console_message = getattr(value, 'console_message', None)
            if console_message:
                cls.console_messages[console_message] = value


MBSConsoleHandler._setup_console_messages()


class MBSLogger:
    def __init__(self):
        self._logger = logging.getLogger("MBS")
        self._level = logging.NOTSET
        self._current_path = os.path.dirname(os.path.realpath(__file__))

    @property
    def logger(self):
        return self._logger

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        self._level = level
        self.logger.setLevel(self._level)

    def setLevel(self, level):
        self.level = level

    def debug(self, *args, **kwargs):
        return self._log_call("debug", args, kwargs)

    def info(self, *args, **kwargs):
        return self._log_call("info", args, kwargs)

    def console(self, *args, **kwargs):
        return self._log_call("info", args, kwargs, console=True)

    def warning(self, *args, **kwargs):
        return self._log_call("warning", args, kwargs)

    def error(self, *args, **kwargs):
        return self._log_call("error", args, kwargs)

    def critical(self, *args, **kwargs):
        return self._log_call("critical", args, kwargs)

    def exception(self, *args, **kwargs):
        return self._log_call("exception", args, kwargs)

    def log(self, *args, **kwargs):
        return self._log_call("log", args, kwargs)

    def _log_call(self, level_name, args, kwargs, console=False):
        caller_filename = inspect.stack()[2][1]
        caller_filename = os.path.normpath(caller_filename)
        if not caller_filename.startswith(self._current_path):
            log_name = "MBS"
        else:
            log_name = "MBS" + caller_filename[len(self._current_path):-3].replace("/", ".")

        if console:
            kwargs.setdefault('extra', {})['console'] = True

        return getattr(logging.getLogger(log_name), level_name)(*args, **kwargs)

    # @console_message decorated methods of MBSConsoleHandler are also propagated
    # as additional methods of this class

    @classmethod
    def _setup_console_message(cls, msg, callback):
        def log_method(self, *args):
            self.console(msg, *args)

        log_method.__name__ = callback.__name__
        setattr(cls, callback.__name__, log_method)

    @classmethod
    def _setup_console_messages(cls):
        for msg, callback in MBSConsoleHandler.console_messages.items():
            cls._setup_console_message(msg, callback)


MBSLogger._setup_console_messages()


def str_to_log_level(level):
    """
    Returns internal representation of logging level defined
    by the string `level`.

    Available levels are: debug, info, warning, error
    """
    if level not in levels:
        return logging.NOTSET

    return levels[level]


def supported_log_backends():
    return ("console", "file")


def init_logging(conf):
    """
    Initializes logging according to configuration file.
    """
    log_backend = conf.log_backend

    if not log_backend or len(log_backend) == 0 or log_backend == "console":
        if conf.system == "mock":
            root_logger = logging.getLogger()
            root_logger.setLevel(conf.log_level)
            handler = MBSConsoleHandler()
            root_logger.addHandler(handler)

            def handle_sigwinch(*args):
                handler.resize()

            signal.signal(signal.SIGWINCH, handle_sigwinch)
        else:
            logging.basicConfig(level=conf.log_level, format=log_format)

        log = MBSLogger()
        log.level = conf.log_level
    else:
        logging.basicConfig(filename=conf.log_file, level=conf.log_level, format=log_format)
        log = MBSLogger()
