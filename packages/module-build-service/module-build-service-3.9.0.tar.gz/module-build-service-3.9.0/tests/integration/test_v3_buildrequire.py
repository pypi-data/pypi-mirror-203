# -*- coding: utf-8 -*-
# SPDX-License-Identifier: MIT


def test_v3_buildrequire(mbs, clone_and_start_build):
    """Test buildrequire fields in the v3-packager mmd.

    Preconditions:
    * 2 contexts defined in mmd, one of which 'build-requires' another module
      (as well as a koji-resolver enabled platform).
    * Build-required module is tagged in koji with koji_tag_with_modules from said platform.

    Steps:
    * Submit a build.
    * Wait until the build(s) are in build state.
    * Cancel the build(s).

    Checks:
    * That that number of builds produced is equal to the number of configurations.
    * That each build has expected buildrequires items.
    """

    repo, builds = clone_and_start_build()
    contexts = {
        cfg["context"]: cfg for cfg in repo.modulemd["data"]["configurations"]
    }

    assert len(builds) == len(contexts)

    for build in builds:
        mbs.wait_for_module_build(build, lambda bld: bld.get("state") >= 2)
        ctx = build.module_build_data["context"]

        assert ctx in contexts
        for buildrequire, data in build.module_build_data["buildrequires"].items():
            if buildrequire == "platform":
                mmd_platform = contexts[ctx]["platform"]
                assert data["stream"] == mmd_platform \
                    if mmd_platform.endswith(".z") else f"{mmd_platform}.z"
                continue
            assert buildrequire in contexts[ctx]["buildrequires"]
            assert data["stream"] == contexts[ctx]["buildrequires"][buildrequire][0]
