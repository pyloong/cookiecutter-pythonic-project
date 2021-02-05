"""Test generated project"""
import pytest
import sh

from tests.conftest import current_python_version


@pytest.mark.parametrize(
    'context_override',
    [
        {'python_version': current_python_version, 'use_pipenv': 'y'},
        {'python_version': current_python_version, 'use_pipenv': 'n'},
        {'python_version': current_python_version, 'init_bootstrap': 'n'},
        {'python_version': current_python_version, 'init_bootstrap': 'y'},
    ],
)
def test_generated_project_tox_cmd(cookies, context_override):
    """Generated project should pass tox."""
    result = cookies.bake(extra_context=context_override)

    try:
        sh.tox(_cwd=str(result.project))  # pylint: disable=no-member
    except sh.ErrorReturnCode as ex:
        pytest.fail(ex.stdout.decode())
