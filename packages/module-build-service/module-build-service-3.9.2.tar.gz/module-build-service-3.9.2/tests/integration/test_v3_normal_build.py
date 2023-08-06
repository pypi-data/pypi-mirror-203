# -*- coding: utf-8 -*-
# SPDX-License-Identifier: MIT


def test_v3_normal_build(mbs, koji, clone_and_start_build):
    """Test a normal module-build submitted with v3-packager YAML modulemd."""

    repo, builds = clone_and_start_build("--optional", "rebuild_strategy=all", cancel=False)
    build = builds[0]

    # actual input (v3 packager mmd)
    assert len(repo.modulemd["data"]["configurations"]) == 1
    mmd_configuration = repo.modulemd["data"]["configurations"][0]
    mmd_context = mmd_configuration["context"]
    mmd_platform = mmd_configuration["platform"]

    mbs.wait_for_module_build_to_succeed(build)

    # assert module build components
    assert sorted(build.component_names()) == sorted(repo.components + ["module-build-macros"])
    for component_rpm in build.components():
        assert koji.get_task(component_rpm["task_id"])["state"] == 2  # is closed

    # assert produced koji build
    koji_build = koji.get_build(build.nvr())
    koji_build_devel = koji.get_build(build.nvr(name_suffix="-devel"))
    assert koji_build and koji_build_devel
    module_data = koji_build['extra']['typeinfo']['module']
    assert module_data['module_build_service_id'] == int(build.id)
    assert module_data['context'] == mmd_context
    koji_mmd = koji.get_modulemd(koji_build)
    actual_platforms = koji_mmd["data"]["dependencies"][0]["buildrequires"]["platform"]
    assert len(actual_platforms) == 1
    assert actual_platforms[0] == f"{mmd_platform}.z"
