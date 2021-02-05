"""Test"""
import os
import re
from pathlib import Path

import pytest
from binaryornot.check import is_binary
from pytest_cookies.plugin import Result

cookiecutter_variable_pattern = re.compile(r'{{(\s?cookiecutter)[.](.*?)}}')

SUPPORTED_COMBINATIONS = [
    {'index_server': 'index_server'},
    {'index_server': 'aliyun'},
    {'index_server': 'tendata'},
    {'use_pipenv': 'n'},
    {'ci_tools': 'none'},
    {'ci_tools': 'Gitlab'},
    {'ci_tools': 'Github'},
    {'use_src_layout': 'y'},
    {'use_src_layout': 'n'},
    {'init_bootstrap': 'n'},
    {'init_bootstrap': 'y'},
]


def _fixture_id(ctx):
    """Helper to get a user friendly test name from the parametrized context."""
    return '-'.join(f'{key}:{value}' for key, value in ctx.items())


def build_files_list(root_dir):
    """Build a list containing absolute paths to the generated files."""
    return [
        os.path.join(dir_path, file_path)
        for dir_path, sub_dirs, files in os.walk(root_dir)
        for file_path in files
    ]


def check_paths(paths):
    """Method to check all paths have correct substitutions."""
    # Assert that no match is found in any of the files
    for path in paths:
        if is_binary(path):
            continue

        for line in open(path, 'r'):
            match = cookiecutter_variable_pattern.search(line)
            msg = 'cookiecutter variable not replaced in {}'
            assert match is None, msg.format(path)


def assert_bake_ok(result: Result):
    """Check bake result is ok"""
    assert result.exit_code == 0
    assert result.project.isdir()
    assert result.project.isdir()


@pytest.mark.parametrize('context_override', SUPPORTED_COMBINATIONS, ids=_fixture_id)
def test_project_generation(cookies, context_override):
    """Test that project is generated and fully rendered."""
    result = cookies.bake(extra_context={**context_override})

    assert_bake_ok(result)

    paths = build_files_list(str(result.project))
    assert paths
    check_paths(paths)


@pytest.mark.parametrize(
    ['use_dicker', 'expected_result'], [("y", [True, True]), ("n", [False, False])]
)
def test_docker_invokes(cookies, use_dicker, expected_result):
    """Test generated project and use docker"""
    result = cookies.bake(extra_context={'use_docker': use_dicker})

    assert_bake_ok(result)

    exist = [
        os.path.isfile(os.path.join(str(result.project), 'Dockerfile')),
        os.path.isfile(os.path.join(str(result.project), '.dockerignore')),
    ]
    assert exist == expected_result


@pytest.mark.parametrize(
    ['use_pipenv', 'index_server', 'expected_result'],
    [
        ('y', 'none', ['Pipfile', 'pypi']),
        ('n', 'none', ['requirements.txt', '']),
        ('y', 'aliyun', ['Pipfile', 'aliyun']),
        ('n', 'aliyun', ['requirements.txt', 'aliyun']),
        ('y', 'tendata', ['Pipfile', 'tendata']),
        ('n', 'tendata', ['requirements.txt', 'tendata']),
    ],
)
def test_index_server_invokes(cookies, use_pipenv, index_server, expected_result):
    """Test generated project"""
    result = cookies.bake(
        extra_context={'use_pipenv': use_pipenv, 'index_server': index_server}
    )

    assert_bake_ok(result)

    assert os.path.isfile(os.path.join(str(result.project), expected_result[0]))
    with open(os.path.join(str(result.project), expected_result[0]), "r") as file:
        data = file.read()
        assert expected_result[1] in data


def has_keyword(filename: Path, keyword: str) -> bool:
    """Check file has keyword"""
    if filename.is_file():
        with open(str(filename), 'r') as file:
            txt = file.read()
            return keyword in txt
    return False


@pytest.mark.parametrize(
    ['use_src_layout', 'except_value'], [('y', True), ('n', False)]
)
def test_use_src_layout_invokes(cookies, use_src_layout, except_value):
    """Test layout"""
    result = cookies.bake(extra_context={'use_src_layout': use_src_layout})

    assert_bake_ok(result)

    assert os.path.exists(os.path.join(result.project, 'src')) == except_value
    assert has_keyword(Path(result.project, 'tox.ini'), 'src') == except_value
    assert has_keyword(Path(result.project, 'setup.cfg'), 'src') == except_value


@pytest.mark.parametrize(['ci_tools', 'expect_value'], [('none', '')])
def test_ci_tools_invokes(cookies, ci_tools, expect_value):
    """Test ci tools"""
    result = cookies.bake(extra_context={'ci_tools': ci_tools})

    assert_bake_ok(result)

    assert os.path.exists(os.path.join(result.project, expect_value))


@pytest.mark.parametrize(
    'init_bootstrap, has_cmdline',
    [
        ('y', True),
        ('n', False)
    ]
)
def test_init_bootstrap(cookies, init_bootstrap, has_cmdline):
    """Test use bootstrap"""
    result = cookies.bake(extra_context={'init_bootstrap': init_bootstrap})

    assert_bake_ok(result)

    exist_cmdline_file = False
    for _, _, files in os.walk(result.project):
        for file in files:
            if file == 'cmdline.py':
                exist_cmdline_file = True
    assert exist_cmdline_file == has_cmdline
    assert has_keyword(Path(result.project, 'setup.cfg'), 'cmdline') == has_cmdline
