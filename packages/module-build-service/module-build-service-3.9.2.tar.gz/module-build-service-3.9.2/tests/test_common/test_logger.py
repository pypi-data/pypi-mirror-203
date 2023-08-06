# -*- coding: utf-8 -*-
# SPDX-License-Identifier: MIT
from __future__ import absolute_import
import io
import logging
import os
from os import path
import re
import pytest
import shutil
import sys
import tempfile
import textwrap
from unittest.mock import patch

from module_build_service.common import log, models
from module_build_service.common.logger import ModuleBuildLogs, MBSConsoleHandler
from module_build_service.scheduler.consumer import MBSConsumer
from module_build_service.scheduler.db_session import db_session


@pytest.fixture()
def test_logger_fixture(request, provide_test_data):
    log.debug(request.function.__module__)
    try:
        # py2
        test_id = ".".join([
            path.splitext(path.basename(__file__))[0],
            request.function.im_class.__name__,
            request.function.im_func.__name__,
        ])
    except AttributeError:
        # py3
        test_id = ".".join([
            path.splitext(path.basename(__file__))[0],
            request.function.__self__.__class__.__name__,
            request.function.__self__.__class__.__name__,
        ])

    base = tempfile.mkdtemp(prefix="mbs-", suffix="-%s" % test_id)
    name_format = "build-{id}.log"
    print("Storing build logs in %r" % base)
    request.cls.build_log = ModuleBuildLogs(base, name_format)
    request.cls.base = base
    yield
    MBSConsumer.current_module_build_id = None
    shutil.rmtree(base)


@pytest.mark.usefixtures("test_logger_fixture")
class TestLogger:

    def test_module_build_logs(self):
        """
        Tests that ModuleBuildLogs is logging properly to build log file.
        """
        build = models.ModuleBuild.get_by_id(db_session, 2)

        # Initialize logging, get the build log path and remove it to
        # ensure we are not using some garbage from previous failed test.
        self.build_log.start(db_session, build)
        path = self.build_log.path(db_session, build)
        assert path[len(self.base):] == "/build-2.log"
        if os.path.exists(path):
            os.unlink(path)

        # Try logging without the MBSConsumer.current_module_build_id set.
        # No log file should be created.
        log.debug("ignore this test msg")
        log.info("ignore this test msg")
        log.warning("ignore this test msg")
        log.error("ignore this test msg")
        assert self.build_log.current_log_stream is sys.stderr
        self.build_log.stop(build)
        assert not os.path.exists(path)

        # Try logging with current_module_build_id set to 1 and then to 2.
        # Only messages with current_module_build_id set to 2 should appear in
        # the log.
        self.build_log.start(db_session, build)
        MBSConsumer.current_module_build_id = 1
        log.debug("ignore this test msg1")
        log.info("ignore this test msg1")
        log.warning("ignore this test msg1")
        log.error("ignore this test msg1")
        assert self.build_log.current_log_stream is sys.stderr

        MBSConsumer.current_module_build_id = 2
        log.debug("ignore this test msg2")
        log.info("ignore this test msg2")
        log.warning("ignore this test msg2")
        log.error("ignore this test msg2")
        self.build_log.current_log_stream.write("ignore this test output2")

        self.build_log.stop(build)
        assert os.path.exists(path)
        with open(path, "r") as f:
            data = f.read()
            # Note that DEBUG is not present unless configured server-wide.
            for level in ["INFO", "WARNING", "ERROR"]:
                assert data.find("MBS - {0} - ignore this test msg2".format(level)) != -1
            assert data.find("ignore this test output2")

        # Try to log more messages when build_log for module 1 is stopped.
        # New messages should not appear in a log.
        MBSConsumer.current_module_build_id = 2
        log.debug("ignore this test msg3")
        log.info("ignore this test msg3")
        log.warning("ignore this test msg3")
        log.error("ignore this test msg3")
        assert self.build_log.current_log_stream is sys.stderr
        self.build_log.stop(build)
        with open(path, "r") as f:
            data = f.read()
            assert data.find("ignore this test msg3") == -1

    def test_module_build_logs_name_format(self):
        build = models.ModuleBuild.get_by_id(db_session, 2)

        log1 = ModuleBuildLogs("/some/path", "build-{id}.log")
        assert log1.name(db_session, build) == "build-2.log"
        assert log1.path(db_session, build) == "/some/path/build-2.log"

        log2 = ModuleBuildLogs("/some/path", "build-{name}-{stream}-{version}.log")
        assert log2.name(db_session, build) == "build-nginx-1-2.log"
        assert log2.path(db_session, build) == "/some/path/build-nginx-1-2.log"


class FakeTerminal(object):
    """
    Just enough terminal to allow meaningfully testing the terminal fanciness
    in MBSConsoleHandler
    """

    def __init__(self):
        self.serializer = FakeTerminalSerializer(self)
        self.reset()
        self.columns = 80
        self.rows = 24

    def get_size(self):
        return os.terminal_size((self.columns, self.rows))

    def isatty(self):
        return True

    def fileno(self):
        return 42

    def flush(self):
        pass

    def write(self, raw):
        for m in re.finditer(r'\n|\033\[[0-9;]*[A-Za-z]|\033|[^\033\n]*', raw):
            piece = m.group(0)
            if piece == '\n':
                self._next_row()
            elif piece == '\033[0m':
                self.cur_attr = "x"
            elif piece == '\033[1m':
                self.cur_attr = self.cur_attr.upper()
            elif piece == '\033[32m':
                self.cur_attr = 'G' if self.cur_attr.isupper() else 'g'
            elif piece == '\033[91m':
                self.cur_attr = 'R' if self.cur_attr.isupper() else 'r'
            elif piece == '\033[0G':
                self.cursor_column = 0
            elif piece == '\033[1A':
                self.cursor_column = 0
                self.cursor_row = max(self.cursor_row - 1, 0)
            elif piece == '\033[2K':
                self.text[self.cursor_row] = ' ' * self.cursor_column
                self.attrs[self.cursor_row] = 'x' * self.cursor_column
            elif piece.startswith('\033['):
                raise RuntimeError("Unhandled CSI sequence: %r", piece)
            else:
                pos = 0
                while len(piece) - pos > self.columns - self.cursor_column:
                    to_insert = self.columns - self.cursor_column
                    self._insert(piece[pos:pos + to_insert])
                    pos += to_insert
                    self._next_row()
                self._insert(piece[pos:])

    def _next_row(self):
        self.cursor_row += 1
        if self.cursor_row == len(self.text):
            self.text.append('')
            self.attrs.append('')
        self.cursor_column = 0

    def _insert(self, string):
        text = self.text[self.cursor_row]
        self.text[self.cursor_row] = (text[0:self.cursor_column]
                                      + string
                                      + text[self.cursor_column + len(string):])
        attrs = self.attrs[self.cursor_row]
        self.attrs[self.cursor_row] = (attrs[0:self.cursor_column]
                                       + self.cur_attr * len(string)
                                       + attrs[self.cursor_column + len(string):])
        self.cursor_column += len(string)

    def reset(self):
        self.text = ['']
        self.attrs = ['']
        self.cur_attr = 'x'
        self.cursor_row = 0
        self.cursor_column = 0

    def serialize(self):
        return self.serializer.serialize()


class FakeTerminalSerializer(object):
    """Serializes the terminal contents with <R></R> tags to represent attributes"""

    def __init__(self, terminal):
        self.terminal = terminal

    def serialize(self):
        self.result = io.StringIO()
        self.last_attr = 'x'

        for row in range(0, len(self.terminal.text)):
            text = self.terminal.text[row]
            attrs = self.terminal.attrs[row]

            for col in range(0, len(text)):
                self.set_attr(attrs[col])
                self.result.write(text[col])
            self.set_attr('x')
            self.result.write('\n')

        value = self.result.getvalue()
        self.result = None

        return value

    def set_attr(self, attr):
        if attr != self.last_attr:
            if self.last_attr != 'x':
                self.result.write('</' + self.last_attr + '>')
            if attr != 'x':
                self.result.write('<' + attr + '>')
            self.last_attr = attr


class TestConsoleHandler:
    def terminal(test_method):
        test_method.terminal = True
        return test_method

    def level(level):
        def decorate(test_method):
            test_method.level = level
            return test_method

        return decorate

    def setup_method(self, test_method):
        if getattr(test_method, 'terminal', False):
            self.stream = FakeTerminal()

            self.get_terminal_size_patcher = patch("os.get_terminal_size")
            mock_get_terminal_size = self.get_terminal_size_patcher.start()

            def get_terminal_size(fileno):
                return self.stream.get_size()

            mock_get_terminal_size.side_effect = get_terminal_size
        else:
            self.stream = io.StringIO()

        self.handler = MBSConsoleHandler(stream=self.stream)
        self.handler.level = getattr(test_method, 'level', logging.INFO)

        logging.getLogger().addHandler(self.handler)

    def teardown_method(self, test_method):
        logging.getLogger().removeHandler(self.handler)

        if getattr(test_method, 'terminal', False):
            self.get_terminal_size_patcher.stop()

    def current(self):
        if isinstance(self.stream, FakeTerminal):
            val = self.stream.serialize()
        else:
            val = self.stream.getvalue()

        return val.rstrip() + '\n'

    def log_messages(self):
        log.debug("Debug")
        log.info("Info")
        log.console("Console")
        log.warning("Warning")
        log.error("Error")

    def test_console_basic(self):
        self.log_messages()

        current = self.current()
        assert "Debug" not in current
        assert "Info" not in current
        assert "Console" in current
        assert "\nWARNING - Warning" in current
        assert "\nERROR - Error" in current

    @terminal
    def test_console_terminal(self):
        self.log_messages()

        current = self.current()
        assert "Debug" not in current
        assert "Info" not in current
        assert "Console" in current
        assert "<R>WARNING</R> - Warning" in current
        assert "<R>ERROR</R> - Error" in current

    @level(logging.DEBUG)
    @terminal
    def test_console_debug(self):
        self.log_messages()

        current = self.current()
        assert "MainThread - MBS - DEBUG - Debug" in current
        assert "MainThread - MBS - INFO - Info" in current
        assert "MainThread - MBS - INFO - Console" in current
        assert "MainThread - MBS - WARNING - Warning" in current
        assert "MainThread - MBS - ERROR - Error" in current

    @terminal
    def test_console_long_running(self):
        log.long_running_start("Frobulating")
        log.long_running_end("Frobulating")
        log.console("---")

        log.long_running_start("Frobulating")
        log.console("Now Hear This")
        log.long_running_end("Frobulating")
        log.console("---")

        log.long_running_start("Frobulating")
        log.long_running_start("Blabbing")
        log.long_running_end("Blabbing")
        log.long_running_end("Frobulating")

        assert self.current() == textwrap.dedent("""\
            Frobulating ... done
            ---
            Frobulating ...
            Now Hear This
            Frobulating ... done
            ---
            Frobulating ...
            Blabbing ... done
            Frobulating ... done
        """)

    @terminal
    def test_console_local_repo(self):
        log.local_repo_start("module-testmodule-build")

        assert self.current() == textwrap.dedent("""\
            <X>module-testmodule-build</X>: Making local repository for Koji tag
            ------------------------------
            <X>module-testmodule-build</X>:
        """)

        log.local_repo_start_downloads("module-testmodule-build", 42, "/tmp/download-dir")
        log.local_repo_start_download("module-testmodule-build",
                                      "https://ftp.example.com/libsomething-1.2.3-1.x86_64.rpm")
        log.local_repo_start_download("module-testmodule-build",
                                      "https://ftp.example.com/libother-1.2.3-1.x86_64.rpm")
        log.local_repo_done_download("module-testmodule-build",
                                     "https://ftp.example.com/libother-1.2.3-1.x86_64.rpm")
        assert self.current() == textwrap.dedent("""\
            <X>module-testmodule-build</X>: Making local repository for Koji tag
            ------------------------------
            <X>module-testmodule-build</X>: Downloading packages 1/42
                libsomething-1.2.3-1.x86_64.rpm
        """)

        log.local_repo_done_download("module-testmodule-build",
                                     "https://ftp.example.com/libsomething-1.2.3-1.x86_64.rpm")
        log.local_repo_done("module-testmodule-build", "downloaded everything")
        assert self.current() == textwrap.dedent("""\
            <X>module-testmodule-build</X>: Making local repository for Koji tag
            <X>module-testmodule-build</X>: <G>downloaded everything</G>
        """)

    @terminal
    def test_console_local_repo_wrap(self):
        log.local_repo_start("module-testmodule-build")
        long_url = "https://ftp.example.com/lib" + (80 * "z") + "-1.2.3-1.x86_64.rpm"
        log.local_repo_start_downloads("module-testmodule-build", 42, "/tmp/download-dir")
        log.local_repo_start_download("module-testmodule-build", long_url)
        assert self.current() == textwrap.dedent("""\
            <X>module-testmodule-build</X>: Making local repository for Koji tag
            ------------------------------
            <X>module-testmodule-build</X>: Downloading packages 0/42
                libzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
            zzzzzzz-1.2.3-1.x86_64.rpm
        """)

        log.local_repo_done_download("module-testmodule-build", long_url)
        log.local_repo_done("module-testmodule-build", "downloaded everything")
        assert self.current() == textwrap.dedent("""\
            <X>module-testmodule-build</X>: Making local repository for Koji tag
            <X>module-testmodule-build</X>: <G>downloaded everything</G>
        """)

    @terminal
    def test_console_partial_line_erase(self):
        self.handler.status_stream.write("Foo\nBar")
        self.handler.status_stream.erase()
        self.handler.status_stream.write("Baz")

        assert self.current() == "Baz\n"

    @terminal
    def test_console_resize(self):
        self.stream.columns = 20
        self.handler.resize()

        self.stream.write("Foo\n")
        self.handler.status_stream.write(30 * "x")
        self.handler.status_stream.erase()
        self.handler.status_stream.write("Baz")

        assert self.current() == "Foo\nBaz\n"
