from builddevenv.Builder import Builder
import pytest
import docker
import os

class TestBuildDevEnv:

    def test_buildenv_ok(self):
        client = docker.from_env()
        builder = Builder(os.path.join(__file__, "test/test_data/env_var.yaml"))
        assert 1 == 1
