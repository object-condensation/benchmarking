from __future__ import annotations

import importlib.metadata

import oc_benchmarking as m


def test_version():
    assert importlib.metadata.version("oc_benchmarking") == m.__version__
