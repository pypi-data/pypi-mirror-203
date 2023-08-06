# -*- coding: utf-8 -*-
# SPDX-License-Identifier: MIT


def test_v3_multiple_contexts(clone_and_start_build):
    """Test that multiple configurations in v3-packager modulemd produce multiple module builds"""
    repo, builds = clone_and_start_build("--optional", "rebuild_strategy=all")
    assert len(builds) == len(repo.modulemd["data"]["configurations"])
