# -*- coding: utf-8 -*-
# SPDX-License-Identifier: MIT
from __future__ import absolute_import, print_function
from collections import defaultdict
import click
import getpass
import logging
import os
import sys

import flask_migrate
from flask.cli import FlaskGroup
from werkzeug.datastructures import FileStorage

from module_build_service import app, db
from module_build_service.builder.MockModuleBuilder import (
    import_builds_from_local_dnf_repos, load_local_builds
)
from module_build_service.common import build_logs, conf, models
from module_build_service.common.errors import StreamAmbigous, StreamNotXyz
from module_build_service.common.utils import load_mmd_file, import_mmd
import module_build_service.scheduler.consumer
from module_build_service.scheduler.db_session import db_session
import module_build_service.scheduler.local
from module_build_service.web.submit import submit_module_build_from_yaml

migrations_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "migrations")
migrate = flask_migrate.Migrate(app, db, directory=migrations_dir)


@click.group(cls=FlaskGroup, create_app=lambda *args, **kwargs: app)
def cli():
    """MBS manager"""


@cli.command("upgradedb")
def upgradedb():
    """ Upgrades the database schema to the latest revision
    """
    app.config["SERVER_NAME"] = "localhost"
    with app.app_context():
        flask_migrate.upgrade(directory=migrations_dir)


def upgradedb_entrypoint():
    """Entrypoint for command mbs-upgradedb"""
    # Work around issue with FlaskGroup not being initiated
    cli(["upgradedb"])


@cli.command("cleardb")
def cleardb():
    """ Clears the database
    """
    models.ModuleBuild.query.delete()
    models.ComponentBuild.query.delete()


@cli.command("import_module")
@click.argument("mmd_file", type=click.Path(exists=True))
def import_module(mmd_file):
    """ Imports the module from mmd_file
    """
    mmd = load_mmd_file(mmd_file)
    import_mmd(db.session, mmd)


def collect_dep_overrides(overrides):
    collected = defaultdict(list)
    for value in overrides:
        parts = value.split(":")
        if len(parts) != 2:
            raise ValueError("dependency overrides must be in the form name:stream")
        name, stream = parts
        collected[name].append(stream)

    return collected


@cli.command("build_module_locally")
@click.option("--stream", metavar="STREAM")
@click.option(
    "--file", "yaml_file",
    metavar="FILE",
    required=True,
    type=click.Path(exists=True),
)
@click.option("--srpm", "srpms", metavar="SRPM", multiple=True)
@click.option("--skiptests", is_flag=True)
@click.option("--offline", is_flag=True)
@click.option(
    '--buildrequires', "buildrequires", multiple=True,
    metavar='name:stream', default=[],
    help='Buildrequires to override in the form of "name:stream"'
)
@click.option(
    '--requires', "requires", multiple=True,
    metavar='name:stream', default=[],
    help='Requires to override in the form of "name:stream"'
)
@click.option("-d", "--debug", "log_debug", is_flag=True)
@click.option(
    "-l", "--add-local-build", "local_build_nsvs",
    metavar="NSV", multiple=True
)
@click.option(
    "-s", "--set-stream", "default_streams",
    metavar="STREAM", multiple=True
)
@click.option(
    "-r", "--platform-repo-file", "platform_repofiles",
    metavar="FILE",
    type=click.Path(exists=True),
    multiple=True
)
@click.option("-p", "--platform-id", metavar="PLATFORM_ID")
def build_module_locally(
    stream=None,
    yaml_file=None,
    srpms=None,
    skiptests=False,
    offline=False,
    log_debug=False,
    local_build_nsvs=None,
    default_streams=None,
    platform_repofiles=None,
    platform_id=None,
    requires=None,
    buildrequires=None,
):
    """ Performs local module build using Mock
    """
    # accumulate initial log messages in memory - we'll output them to a log in the
    # module build directories when we know what they are
    build_logs.buffer_initially()

    # if debug is not specified, set log level of console to INFO
    if log_debug:
        for handler in logging.getLogger().handlers:
            handler.setLevel(logging.DEBUG)

    if "SERVER_NAME" not in app.config or not app.config["SERVER_NAME"]:
        app.config["SERVER_NAME"] = "localhost"

        if conf.resolver == "db":
            raise ValueError(
                "Please set RESOLVER to 'mbs' in your configuration for local builds.")

    conf.set_item("system", "mock")
    conf.set_item("base_module_repofiles", platform_repofiles)

    # Use our own local SQLite3 database.
    confdir = os.path.abspath(os.getcwd())
    dbdir = \
        os.path.abspath(os.path.join(confdir, "..")) if confdir.endswith("conf") else confdir
    dbpath = "/{0}".format(os.path.join(dbdir, ".mbs_local_build.db"))
    dburi = "sqlite://" + dbpath
    app.config["SQLALCHEMY_DATABASE_URI"] = dburi
    conf.set_item("sqlalchemy_database_uri", dburi)
    if os.path.exists(dbpath):
        os.remove(dbpath)

    db.create_all()
    # Reconfigure the backend database session registry to use the new the database location
    db_session.remove()
    db_session.configure(bind=db.session.bind)

    params = {
        "local_build": True,
        "default_streams": dict(ns.split(":") for ns in default_streams),
        "require_overrides": collect_dep_overrides(requires),
        "buildrequire_overrides": collect_dep_overrides(buildrequires),
    }
    if srpms:
        params["srpms"] = srpms

    username = getpass.getuser()
    if not yaml_file or not yaml_file.endswith(".yaml"):
        raise IOError("Provided modulemd file is not a yaml file.")

    yaml_file_path = os.path.abspath(yaml_file)

    if offline:
        import_builds_from_local_dnf_repos(platform_id)
    load_local_builds(local_build_nsvs)

    with open(yaml_file_path) as fd:
        filename = os.path.basename(yaml_file)
        handle = FileStorage(fd)
        handle.filename = filename
        try:
            module_builds = submit_module_build_from_yaml(
                db_session, username, handle, params,
                stream=str(stream), skiptests=skiptests
            )
        except StreamAmbigous as e:
            logging.error(str(e))
            logging.error("Use '-s module_name:module_stream' to choose the stream")
            return 1
        except StreamNotXyz as e:
            logging.error(str(e))
            logging.error("Use '--buildrequires name:stream' to override the base module stream")
            return 1

        module_build_ids = [build.id for build in module_builds]

    try:
        module_build_service.scheduler.local.main(module_build_ids)
    except module_build_service.scheduler.local.BuildFailed as e:
        logging.error("%s", e)
        sys.exit(1)


@cli.command("retire")
@click.argument("identifier", metavar="NAME:STREAM[:VERSION[:CONTEXT]]")
@click.option(
    "--confirm",
    is_flag=True,
    default=False,
    help="Perform retire operation without prompting",
)
def retire(identifier, confirm=False):
    """ Retire module build(s) by placing them into 'garbage' state.
    """
    # Parse identifier and build query
    parts = identifier.split(":")
    if len(parts) < 2:
        raise ValueError("Identifier must contain at least NAME:STREAM")
    if len(parts) >= 5:
        raise ValueError("Too many parts in identifier")

    filter_by_kwargs = {"state": models.BUILD_STATES["ready"], "name": parts[0], "stream": parts[1]}

    if len(parts) >= 3:
        filter_by_kwargs["version"] = parts[2]
    if len(parts) >= 4:
        filter_by_kwargs["context"] = parts[3]

    # Find module builds to retire
    module_builds = db_session.query(models.ModuleBuild).filter_by(**filter_by_kwargs).all()

    if not module_builds:
        logging.info("No module builds found.")
        return

    logging.info("Found %d module builds:", len(module_builds))
    for build in module_builds:
        logging.info("\t%s", ":".join((build.name, build.stream, build.version, build.context)))

    # Prompt for confirmation
    confirm_msg = "Retire {} module builds?".format(len(module_builds))
    is_confirmed = confirm or click.confirm(confirm_msg, abort=False)
    if not is_confirmed:
        logging.info("Module builds were NOT retired.")
        return

    # Retire module builds
    for build in module_builds:
        build.transition(
            db_session, conf, models.BUILD_STATES["garbage"], "Module build retired")

    db_session.commit()

    logging.info("Module builds retired.")


@cli.command("run")
@click.option("-h", "--host", metavar="HOST", help="Bind to this host.")
@click.option("-p", "--port", metavar="PORT", help="Bind to this port along with --host.")
@click.option("-d", "--debug", is_flag=True, default=False, help="Run frontend in debug mode.")
def run(host=None, port=None, debug=None):
    """ Runs the Flask app, locally. Intended for dev instances, should not be used for production.
    """
    host = host or conf.host
    port = port or conf.port
    debug = debug or conf.debug

    logging.info("Starting Module Build Service frontend")

    app.run(host=host, port=port, debug=debug)


if __name__ == "__main__":
    cli()
