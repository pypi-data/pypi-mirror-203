# -*- coding: utf-8 -*-
# SPDX-License-Identifier: MIT
from __future__ import absolute_import
import os
import tempfile
import shutil
from textwrap import dedent

import kobo.rpmlib
import koji
import mock
import pytest

from module_build_service.common.config import conf
from module_build_service.builder.base import GenericBuilder
from module_build_service.builder.MockModuleBuilder import (
    import_fake_base_module,
    import_builds_from_local_dnf_repos,
    load_local_builds,
    MockModuleBuilder,
)
from module_build_service.common import models
from module_build_service.common.models import ModuleBuild, ComponentBuild
from module_build_service.common.utils import import_mmd, load_mmd, mmd_to_str
from module_build_service.scheduler import events
from module_build_service.scheduler.db_session import db_session
from tests import make_module_in_db, read_staged_data, staged_data_filename


class TestConfig(object):
    def __init__(self, resultsdir):
        self.resultsdir = resultsdir


@pytest.fixture
def testconfig():
    resultsdir = tempfile.mkdtemp()

    with mock.patch.multiple("module_build_service.common.conf",
                             mock_resultsdir=resultsdir,
                             system="mock"):
        yield TestConfig(resultsdir)


@pytest.mark.usefixtures("require_empty_database", "testconfig")
class TestMockModuleBuilder:
    def setup_method(self, test_method):
        self.resultdir = tempfile.mkdtemp()

    def teardown_method(self, test_method):
        shutil.rmtree(self.resultdir)

    def _create_module_with_filters(self, db_session, batch, state):
        mmd = load_mmd(read_staged_data("testmodule-with-filters"))
        # Set the name and stream
        mmd = mmd.copy("mbs-testmodule", "test")
        mmd.set_xmd({
            "mbs": {
                "rpms": {
                    "ed": {"ref": "01bf8330812fea798671925cc537f2f29b0bd216"},
                    "mksh": {"ref": "f70fd11ddf96bce0e2c64309706c29156b39141d"},
                },
                "buildrequires": {
                    "host": {
                        "version": "20171024133034",
                        "filtered_rpms": [],
                        "stream": "master",
                        "ref": "6df253bb3c53e84706c01b8ab2d5cac24f0b6d45",
                        "context": "00000000",
                    },
                    "platform": {
                        "version": "20171028112959",
                        "filtered_rpms": [],
                        "stream": "master",
                        "ref": "4f7787370a931d57421f9f9555fc41c3e31ff1fa",
                        "context": "00000000",
                    },
                },
                "scmurl": "file:///testdir",
                "commit": "5566bc792ec7a03bb0e28edd1b104a96ba342bd8",
                "requires": {
                    "platform": {
                        "version": "20171028112959",
                        "filtered_rpms": [],
                        "stream": "master",
                        "ref": "4f7787370a931d57421f9f9555fc41c3e31ff1fa",
                        "context": "00000000",
                    }
                },
            }
        })
        module = ModuleBuild.create(
            db_session,
            conf,
            name="mbs-testmodule",
            stream="test",
            version="20171027111452",
            modulemd=mmd_to_str(mmd),
            scmurl="file:///testdir",
            username="test",
        )
        module.koji_tag = "module-mbs-testmodule-test-20171027111452"
        module.batch = batch
        db_session.add(module)
        db_session.commit()

        comp_builds = [
            {
                "module_id": module.id,
                "state": state,
                "package": "ed",
                "format": "rpms",
                "scmurl": (
                    "https://src.fedoraproject.org/rpms/ed"
                    "?#01bf8330812fea798671925cc537f2f29b0bd216"
                ),
                "batch": 2,
                "ref": "01bf8330812fea798671925cc537f2f29b0bd216",
            },
            {
                "module_id": module.id,
                "state": state,
                "package": "mksh",
                "format": "rpms",
                "scmurl": (
                    "https://src.fedoraproject.org/rpms/mksh"
                    "?#f70fd11ddf96bce0e2c64309706c29156b39141d"
                ),
                "batch": 3,
                "ref": "f70fd11ddf96bce0e2c64309706c29156b39141d",
            },
        ]

        for build in comp_builds:
            db_session.add(ComponentBuild(**build))
        db_session.commit()

        return module

    def test_createrepo_filter_last_batch(self):
        module = self._create_module_with_filters(db_session, 3, koji.BUILD_STATES["COMPLETE"])

        builder = MockModuleBuilder(
            db_session, "mcurlej", module, conf, module.koji_tag, module.component_builds
        )
        builder.resultsdir = self.resultdir
        rpms = [
            "ed-1.14.1-4.module+24957a32.x86_64.rpm",
            "mksh-56b-1.module+24957a32.x86_64.rpm",
            "module-build-macros-0.1-1.module+24957a32.noarch.rpm",
        ]
        rpm_qf_output = dedent("""\
            ed 0 1.14.1 4.module+24957a32 x86_64
            mksh 0 56b 1.module+24957a32 x86_64
            module-build-macros 0 0.1 1.module+24957a32 noarch
        """)
        with mock.patch("os.listdir", return_value=rpms):
            with mock.patch("subprocess.check_output", return_value=rpm_qf_output):
                builder._createrepo()

        with open(os.path.join(self.resultdir, "pkglist"), "r") as fd:
            pkglist = fd.read().strip()
            rpm_names = [kobo.rpmlib.parse_nvr(rpm)["name"] for rpm in pkglist.split("\n")]
            assert "ed" not in rpm_names

    def test_createrepo_not_last_batch(self):
        module = self._create_module_with_filters(db_session, 2, koji.BUILD_STATES["COMPLETE"])

        builder = MockModuleBuilder(
            db_session, "mcurlej", module, conf, module.koji_tag, module.component_builds
        )
        builder.resultsdir = self.resultdir
        rpms = [
            "ed-1.14.1-4.module+24957a32.x86_64.rpm",
            "mksh-56b-1.module+24957a32.x86_64.rpm",
        ]
        rpm_qf_output = dedent("""\
            ed 0 1.14.1 4.module+24957a32 x86_64
            mksh 0 56b 1.module+24957a32 x86_64
        """)
        with mock.patch("os.listdir", return_value=rpms):
            with mock.patch("subprocess.check_output", return_value=rpm_qf_output):
                builder._createrepo()

        with open(os.path.join(self.resultdir, "pkglist"), "r") as fd:
            pkglist = fd.read().strip()
            rpm_names = [kobo.rpmlib.parse_nvr(rpm)["name"] for rpm in pkglist.split("\n")]
            assert "ed" in rpm_names

    def test_createrepo_empty_rmp_list(self):
        module = self._create_module_with_filters(db_session, 3, koji.BUILD_STATES["COMPLETE"])

        builder = MockModuleBuilder(
            db_session, "mcurlej", module, conf, module.koji_tag, module.component_builds)
        builder.resultsdir = self.resultdir
        rpms = []
        with mock.patch("os.listdir", return_value=rpms):
            builder._createrepo()

        with open(os.path.join(self.resultdir, "pkglist"), "r") as fd:
            pkglist = fd.read().strip()
            assert not pkglist


@pytest.mark.usefixtures("testconfig")
class TestMockModuleBuilderBuild:
    @pytest.fixture
    def testsetup(self, require_platform_and_default_arch):
        mmd = load_mmd(read_staged_data("formatted_testmodule"))
        xmd = mmd.get_xmd()
        xmd["mbs"]["koji_tag"] = "module-testmodule-master-20180205135154-9c690d0e"
        mmd.set_xmd(xmd)

        import_mmd(db_session, mmd)

        build = ModuleBuild.get_last_build_in_stream(db_session, "testmodule", "master")
        build.batch = 2

        comp_builds = [
            {
                "module_id": build.id,
                "state": koji.BUILD_STATES["COMPLETE"],
                "package": "module-build-macros",
                "nvr": "module-build-macros-0.1-1.module+f33+2+cea92c88",
                "format": "rpms",
                "batch": 1,
                "scmurl": ("/tmp/module_build_service-build-macrosWZUPeK/SRPMS/"
                           "module-build-macros-0.1-1.src.rpm"),
            },
            {
                "module_id": build.id,
                "state": koji.BUILD_STATES["BUILDING"],
                "package": "perl-Tangerine",
                "format": "rpms",
                "scmurl": (
                    "https://src.fedoraproject.org/rpms/perl-Tangerine?#master"
                ),
                "batch": 2,
                "ref": "01234567812fea798671925cc537f2f29b0bd216",
            },
        ]

        for build in comp_builds:
            db_session.add(ComponentBuild(**build))

        db_session.commit()

    @pytest.fixture(params=[{}])
    def mock_external_commands(self, request):
        def mock_popen(cmd, *args, **kwargs):
            stdout = kwargs.get("stdout", None)

            result = mock.MagicMock(name="Popen")
            result.__enter__.return_value = result
            result.communicate.return_value = (None, None)
            result.poll.return_value = 0
            result.returncode = 0

            command = os.path.basename(cmd[0])
            if command == "mock":
                if "--init" in cmd:
                    return result

                result.returncode = 1 if "fail_build" in request.param else 0

                resultdir = None
                for arg in cmd:
                    if arg.startswith("--resultdir="):
                        resultdir = arg[len("--resultdir="):]
                assert resultdir

                result_files = [
                    "perl-Tangerine-0.22-2.module_1589+0def5cd9.src.rpm",
                    "perl-Tangerine-0.22-2.module_1589+0def5cd9.noarch.rpm"
                ]

                if stdout:
                    stdout.write("Successfully built perl-Tangerine")
                    stdout.flush()

                for f in result_files:
                    with open(os.path.join(resultdir, f), "w") as f:
                        f.write("-")

                return result
            elif command == "createrepo_c":
                # Expecting /usr/bin/createrepo_c --pkglist <pkglist> <path>
                assert len(cmd) == 4
                assert cmd[0:2] == ["/usr/bin/createrepo_c", "--pkglist"]
                path = cmd[3]

                repodata_path = os.path.join(path, "repodata")
                if not os.path.exists(repodata_path):
                    os.mkdir(repodata_path)
                with open(os.path.join(repodata_path, "repomd.xml"), "w") as f:
                    f.write("-")

                return result
            elif command == "modifyrepo_c":
                return result
            elif command == "rpm":
                assert cmd[0:4] == [
                    "rpm",
                    "--queryformat",
                    "%{NAME} %{EPOCHNUM} %{VERSION} %{RELEASE} %{ARCH}\n",
                    "-qp"
                ]
                packages = cmd[4:]
                ret = ""
                for p in packages:
                    nvr, arch, ext = p.rsplit(".", 2)
                    n, v, r = nvr.rsplit("-", 2)
                    ret += "{} 0 {} {} {}\n".format(n, v, r, arch)

                result.communicate.return_value = (ret, None)

                return result
            else:
                raise RuntimeError("Unsupported cmd {}".format(cmd))

        with mock.patch("subprocess.Popen") as popen_mock:
            popen_mock.side_effect = mock_popen
            yield

    def make_builder(self):
        build = ModuleBuild.get_last_build_in_stream(db_session, "testmodule", "master")

        # This is used to identify the first build of a module
        MockModuleBuilder._build_id = 1

        builder = GenericBuilder.create_from_module(db_session, build, conf, buildroot_connect=True)

        builder.buildroot_add_artifacts([
            "module-build-macros-0.1-1.module+f33+2+cea92c88"
        ])

        return builder

    @pytest.fixture(params=[{}])
    def builder(self, mock_external_commands, testsetup):
        builder = self.make_builder()

        yield builder

        builder.finalize(succeeded=True)

    def test_mock_module_builder_build(self, builder):
        builder.build("perl-Tangerine", "https://src.fedoraproject.org/rpms/perl-Tangerine?#master")

        # Try building again to exercise code to clean up last build for this thread
        builder.build("perl-Tangerine", "https://src.fedoraproject.org/rpms/perl-Tangerine?#master")

    @pytest.mark.parametrize("mock_external_commands", [{"fail_build": True}], indirect=True)
    def test_mock_module_builder_build_failure(self, builder, caplog):
        builder.build("perl-Tangerine", "file://opt/sources/fedora/perl-Tangerine?#master")
        assert "Error while building artifact perl-Tangerine" in caplog.text

    def test_mock_module_builder_build_local_repo(self, builder):
        builder.build("perl-Tangerine", "file://opt/sources/fedora/perl-Tangerine?#master")

    def test_mock_module_builder_build_srpm(self, builder):
        builder.build("perl-Tangerine", "/opt/sources/perl-Tangerine-0.22-2.src.rpm")

    def test_mock_module_builder_build_stale_builddir(self, mock_external_commands):
        builder = self.make_builder()
        try:
            builder.build("perl-Tangerine", "/opt/sources/perl-Tangerine-0.22-2.src.rpm")
        finally:
            builder.finalize(succeeded=True)

        builder2 = self.make_builder()
        try:
            builder2.build("perl-Tangerine", "/opt/sources/perl-Tangerine-0.22-2.src.rpm")
        finally:
            builder.finalize(succeeded=True)


@pytest.mark.usefixtures("require_empty_database", "testconfig")
class TestMockModuleBuilderAddRepos:
    @pytest.fixture
    def testsetup(self):
        import_fake_base_module("platform:f29:1:000000")

        platform = ModuleBuild.get_last_build_in_stream(db_session, "platform", "f29")
        module_deps = [{
            "requires": {"platform": ["f29"]},
            "buildrequires": {"platform": ["f29"]},
        }]
        foo = make_module_in_db("foo:1:1:1", module_deps)
        app = make_module_in_db("app:1:1:1", module_deps)

        builder = MockModuleBuilder(db_session, "user", app, conf, "module-app", [])

        with mock.patch.multiple("module_build_service.builder.MockModuleBuilder.MockModuleBuilder",
                                 _load_mock_config=mock.MagicMock(),
                                 _write_mock_config=mock.MagicMock()):
            yield {
                "builder": builder,
                "platform": platform,
                "app": app,
                "foo": foo,
            }

    @mock.patch(
        "module_build_service.common.config.Config.base_module_repofiles",
        new_callable=mock.PropertyMock,
        return_value=["/etc/yum.repos.d/bar.repo", "/etc/yum.repos.d/bar-updates.repo"],
        create=True,
    )
    @mock.patch("module_build_service.builder.MockModuleBuilder.open", create=True)
    def test_buildroot_add_repos_repofile(self, patched_open, base_module_repofiles, testsetup):
        builder = testsetup["builder"]
        platform = testsetup["platform"]
        foo = testsetup["foo"]
        app = testsetup["app"]

        patched_open.side_effect = [
            mock.mock_open(read_data="[fake]\nrepofile 1\n").return_value,
            mock.mock_open(read_data="[fake]\nrepofile 2\n").return_value,
            mock.mock_open(read_data="[fake]\nrepofile 3\n").return_value,
        ]

        dependencies = {
            "repofile://": [platform.mmd()],
            "repofile:///etc/yum.repos.d/foo.repo": [foo.mmd(), app.mmd()],
        }

        builder.buildroot_add_repos(dependencies)

        assert "repofile 1" in builder.yum_conf
        assert "repofile 2" in builder.yum_conf
        assert "repofile 3" in builder.yum_conf

        assert set(builder.enabled_modules) == {"foo:1", "app:1"}

    def test_buildroot_add_repos_local(self, testsetup):
        builder = testsetup["builder"]
        foo = testsetup["foo"]

        dependencies = {
            os.path.join(conf.mock_resultsdir, "module-foo/results"): [foo.mmd()]
        }

        builder.buildroot_add_repos(dependencies)

        assert "[foo]" in builder.yum_conf

        assert set(builder.enabled_modules) == set()

    @mock.patch("koji.ClientSession")
    def test_buildroot_add_repos_koji_tag_with_repo(self, client_session, testsetup):
        builder = testsetup["builder"]
        foo = testsetup["foo"]

        client_session_mock = mock.MagicMock()
        client_session.return_value = client_session_mock

        client_session_mock.getRepo.return_value = {
            "id": 2471511
        }

        dependencies = {
            "module-foo": [foo.mmd()]
        }

        builder.buildroot_add_repos(dependencies)

        assert "[module-foo]" in builder.yum_conf
        assert ("baseurl=https://kojipkgs.stg.fedoraproject.org"
                "//repos/module-foo/2471511/x86_64/" in builder.yum_conf)

        assert set(builder.enabled_modules) == set()

    @pytest.mark.parametrize("should_add_repo", (True, False))
    @mock.patch("koji.ClientSession")
    @mock.patch("module_build_service.builder.MockModuleBuilder.create_local_repo_from_koji_tag")
    def test_buildroot_add_repos_koji_tag_create_local_repo(
            self, create_local_repo, client_session, testsetup, should_add_repo
    ):
        builder = testsetup["builder"]
        foo = testsetup["foo"]

        import_fake_base_module("platform:f29:1:000000")

        client_session_mock = mock.MagicMock()
        client_session.return_value = client_session_mock

        client_session_mock.getRepo.return_value = None
        client_session_mock.getTagExternalRepos.return_value = [{
            "external_repo_name": "extdep",
            "url": "http://example.com/repos/extdep",
        }]

        create_local_repo.return_value = should_add_repo

        dependencies = {
            "module-foo": [foo.mmd()]
        }

        builder.buildroot_add_repos(dependencies)

        if should_add_repo:
            assert "[module-foo]" in builder.yum_conf
            assert ("baseurl=file:///tmp/mbs/koji_tags/module-foo" in builder.yum_conf)
        else:
            assert "[module-foo]" not in builder.yum_conf

        assert "[extdep]" in builder.yum_conf
        assert ("baseurl=http://example.com/repos/extdep" in builder.yum_conf)

        assert set(builder.enabled_modules) == set()


@pytest.mark.usefixtures("require_empty_database_cls")
class TestOfflineLocalBuilds:

    def test_import_fake_base_module(self):
        import_fake_base_module("platform:foo:1:000000")
        module_build = models.ModuleBuild.get_build_from_nsvc(
            db_session, "platform", "foo", 1, "000000")
        assert module_build

        mmd = module_build.mmd()
        xmd = mmd.get_xmd()
        assert xmd == {
            "mbs": {
                "buildrequires": {},
                "commit": "ref_000000",
                "koji_tag": "repofile://",
                "mse": "true",
                "requires": {},
            }
        }

        assert set(mmd.get_profile_names()) == {"buildroot", "srpm-buildroot"}

    @mock.patch(
        "module_build_service.builder.MockModuleBuilder.open",
        create=True,
        new_callable=mock.mock_open,
    )
    def test_import_builds_from_local_dnf_repos(self, patched_open):
        with mock.patch("dnf.Base") as dnf_base:
            repo = mock.MagicMock()
            repo.repofile = "/etc/yum.repos.d/foo.repo"
            mmd = load_mmd(read_staged_data("formatted_testmodule"))
            repo.get_metadata_content.return_value = mmd_to_str(mmd)
            base = dnf_base.return_value
            base.repos = {"reponame": repo}
            patched_open.return_value.readlines.return_value = ("FOO=bar", "PLATFORM_ID=platform:x")

            import_builds_from_local_dnf_repos()

            base.read_all_repos.assert_called_once()
            repo.load.assert_called_once()
            repo.get_metadata_content.assert_called_once_with("modules")

            module_build = models.ModuleBuild.get_build_from_nsvc(
                db_session, "testmodule", "master", 20180205135154, "9c690d0e")
            assert module_build
            assert module_build.koji_tag == "repofile:///etc/yum.repos.d/foo.repo"

            module_build = models.ModuleBuild.get_build_from_nsvc(
                db_session, "platform", "x", 1, "000000")
            assert module_build

    def test_import_builds_from_local_dnf_repos_platform_id(self):
        with mock.patch("dnf.Base"):
            import_builds_from_local_dnf_repos("platform:y")

            module_build = models.ModuleBuild.get_build_from_nsvc(
                db_session, "platform", "y", 1, "000000")
            assert module_build


@mock.patch(
    "module_build_service.common.config.Config.mock_resultsdir",
    new_callable=mock.PropertyMock,
    return_value=staged_data_filename("local_builds")
)
@mock.patch(
    "module_build_service.common.config.Config.system",
    new_callable=mock.PropertyMock,
    return_value="mock",
)
@pytest.mark.usefixtures("require_empty_database")
class TestLocalBuilds:

    def setup_method(self):
        events.scheduler.reset()

    def teardown_method(self):
        events.scheduler.reset()

    def test_load_local_builds_name(self, conf_system, conf_resultsdir):
        load_local_builds("testmodule")
        local_modules = models.ModuleBuild.local_modules(db_session)

        assert len(local_modules) == 1
        assert local_modules[0].koji_tag.endswith(
            "/module-testmodule-master-20170816080816/results")

    def test_load_local_builds_name_stream(self, conf_system, conf_resultsdir):
        load_local_builds("testmodule:master")
        local_modules = models.ModuleBuild.local_modules(db_session)

        assert len(local_modules) == 1
        assert local_modules[0].koji_tag.endswith(
            "/module-testmodule-master-20170816080816/results")

    def test_load_local_builds_name_stream_non_existing(
        self, conf_system, conf_resultsdir
    ):
        with pytest.raises(RuntimeError):
            load_local_builds("testmodule:x")
            models.ModuleBuild.local_modules(db_session)

    def test_load_local_builds_name_stream_version(self, conf_system, conf_resultsdir):
        load_local_builds("testmodule:master:20170816080815")
        local_modules = models.ModuleBuild.local_modules(db_session)

        assert len(local_modules) == 1
        assert local_modules[0].koji_tag.endswith(
            "/module-testmodule-master-20170816080815/results")

    def test_load_local_builds_name_stream_version_non_existing(
        self, conf_system, conf_resultsdir
    ):
        with pytest.raises(RuntimeError):
            load_local_builds("testmodule:master:123")
            models.ModuleBuild.local_modules(db_session)

    def test_load_local_builds_platform(self, conf_system, conf_resultsdir):
        load_local_builds("platform:f30")
        local_modules = models.ModuleBuild.local_modules(db_session)

        assert len(local_modules) == 1
        assert local_modules[0].koji_tag.endswith("/module-platform-f30-3/results")

    def test_load_local_builds_platform_f28(self, conf_system, conf_resultsdir):
        load_local_builds("platform:f30")
        local_modules = models.ModuleBuild.local_modules(db_session)

        assert len(local_modules) == 1
        assert local_modules[0].koji_tag.endswith("/module-platform-f30-3/results")
