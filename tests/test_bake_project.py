from contextlib import contextmanager

import pytest_cookies
from cookiecutter.utils import rmtree


@contextmanager
def bake_in_temp_dir(cookies: pytest_cookies.Cookies, *args: str, **kwargs: int) -> pytest_cookies.Result:
    """
    Delete the temporal directory that is created when executing the tests
    :param cookies: pytest_cookies.Cookies,
        cookie to be baked and its temporal files will be removed
    """
    result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally:
        rmtree(str(result.project))


def test_bake_with_defaults(cookies) -> None:
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        assert result.exit_code == 0
        assert result.exception is None

        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert 'README.md' in found_toplevel_files
        assert 'Makefile' in found_toplevel_files
        assert 'docker-compose.yml' in found_toplevel_files
        assert 'ops' in found_toplevel_files
        assert 'backend' in found_toplevel_files
        assert 'nginx' in found_toplevel_files
        assert '.pre-commit-config.yaml' in found_toplevel_files
        assert '.gitignore' in found_toplevel_files
        assert '.env' in found_toplevel_files
