"""Test generated project"""
import pytest
import sh
from pytest_cookies.plugin import Cookies

from tests.conftest import current_python_version


@pytest.mark.parametrize(
    'context_override',
    [
        {'python_version': current_python_version, 'use_poetry': 'n'},
        {'python_version': current_python_version, 'use_poetry': 'y'},
        {'python_version': current_python_version, 'init_skeleton': 'n'},
        {'python_version': current_python_version, 'init_skeleton': 'y'},
    ],
)
def test_generated_project_tox_cmd(cookies: Cookies, context_override):
    """Generated project should pass tox."""
    result = cookies.bake(extra_context=context_override)
    cwd = str(result.project_path)

    try:
        sh.tox(_cwd=cwd)  # pylint: disable=no-member
    except sh.ErrorReturnCode as ex:
        pytest.fail(ex.stderr.decode())
