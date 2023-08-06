# -*- coding: utf-8 -*-
# SPDX-License-Identifier: MIT


def test_v3_no_components(mbs, clone_and_start_build):
    """Test a minimal mmd - with no  RPM components"""
    _, builds = clone_and_start_build(cancel=False)
    assert len(builds) == 1
    build = builds[0]

    mbs.wait_for_module_build_to_succeed(build)
    assert not build.data["component_builds"]
