"""Test"""
from __future__ import annotations

import os
import re
from pathlib import Path

import pytest
from binaryornot.check import is_binary
from pytest_cookies.plugin import Cookies, Result

cookiecutter_variable_pattern = re.compile(r'{{(\s?cookiecutter)[.](.*?)}}')

SUPPORTED_COMBINATIONS = [
    {'index_server': 'index_server'},
    {'use_poetry': 'n'},
    {'ci_tools': 'none'},
    {'ci_tools': 'Gitlab'},
    {'ci_tools': 'Github'},
    {'use_src_layout': 'y'},
    {'use_src_layout': 'n'},
    {'init_skeleton': 'n'},
    {'init_skeleton': 'y'},
]


def _fixture_id(ctx):
    """Helper to get a friendly test name from the parametrized context."""
    return '-'.join(f'{key}:{value}' for key, value in ctx.items())


def build_files_list(root_dir: Path):
    """Build a list containing absolute paths to the generated files."""
    return [
        Path(dir_path) / file_path
        for dir_path, sub_dirs, files in os.walk(root_dir)
        for file_path in files
    ]


def check_paths(paths: list[Path]):
    """Method to check all paths have correct substitutions."""
    # Assert that no match is found in any of the files
    for path in paths:
        if is_binary(str(path)):
            continue
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                match = cookiecutter_variable_pattern.search(line)
                msg = 'cookiecutter variable not replaced in {}'
                assert match is None, msg.format(path)


def assert_has_file(file: Path, expect_value):
    """assert file exist factory"""
    assert file.exists() == expect_value


def has_keyword(file: Path, keyword: str) -> bool:
    """Check file has keyword"""
    if file.is_file():
        with open(file, 'r', encoding='utf-8') as reader:
            txt = reader.read()
            return keyword in txt
    return False


def assert_bake_ok(result: Result):
    """Check bake result is ok"""
    assert result.exit_code == 0
    assert result.project_path.is_dir()


@pytest.mark.parametrize('context_override', SUPPORTED_COMBINATIONS, ids=_fixture_id)
def test_project_generation(cookies: Cookies, context_override):
    """Test that project is generated and fully rendered."""
    result = cookies.bake(extra_context={**context_override})

    assert_bake_ok(result)

    paths = build_files_list(result.project_path)
    assert paths
    check_paths(paths)


@pytest.mark.parametrize(
    ['project_name', 'expected_result'],
    [
        ('', 'my_project'),
        ('My Project', 'my_project'),
        (' My Project', 'my_project'),
        ('My Project ', 'my_project'),
        (' My Project ', 'my_project'),
        ('  My Project ', 'my_project'),
    ]
)
def test_check_project_slug(cookies: Cookies, project_name, expected_result):
    """Test check project_slug has spaces."""
    extra_context = {'use_src_layout': 'n'}
    if project_name:
        extra_context.update({'project_name': project_name})
    result = cookies.bake(extra_context=extra_context)
    package_path = result.project_path / expected_result
    assert package_path.exists()


@pytest.mark.parametrize(
    'use_poetry, has_poetry_keyword, required_files',
    [
        ('y', True, False),
        ('n', False, True),
    ]
)
def test_use_poetry(
        cookies: Cookies,
        use_poetry,
        has_poetry_keyword,
        required_files,
):
    """test use poetry"""
    result = cookies.bake(extra_context={'use_poetry': use_poetry})
    assert_bake_ok(result)
    assert has_keyword(result.project_path / 'pyproject.toml', 'poetry') == has_poetry_keyword
    assert_has_file(result.project_path / 'MANIFEST.in', required_files)
    assert_has_file(result.project_path / 'setup.cfg', required_files)
    assert_has_file(result.project_path / 'requirements.txt', required_files)


@pytest.mark.parametrize(
    ['use_dicker', 'expected_result'], [("y", [True, True]), ("n", [False, False])]
)
def test_docker_invokes(cookies: Cookies, use_dicker, expected_result):
    """Test generated project and use docker"""
    result = cookies.bake(extra_context={'use_docker': use_dicker})

    assert_bake_ok(result)

    exist = [
        os.path.isfile(result.project_path / 'Dockerfile'),
        os.path.isfile(result.project_path / '.dockerignore'),
    ]
    assert exist == expected_result


@pytest.mark.parametrize(
    ['use_src_layout', 'except_value'], [('y', True), ('n', False)]
)
def test_use_src_layout_invokes(cookies: Cookies, use_src_layout, except_value):
    """Test layout"""
    result = cookies.bake(extra_context={'use_src_layout': use_src_layout})

    assert_bake_ok(result)

    assert (result.project_path / 'src').exists() == except_value
    assert has_keyword(result.project_path / 'tox.ini', 'src') == except_value


@pytest.mark.parametrize(['ci_tools', 'expect_value'], [('none', '')])
def test_ci_tools_invokes(cookies: Cookies, ci_tools, expect_value):
    """Test ci tools"""
    result = cookies.bake(extra_context={'ci_tools': ci_tools})
    assert_bake_ok(result)

    assert os.path.exists(result.project_path / expect_value)


@pytest.mark.parametrize(
    'init_skeleton, has_cmdline',
    [
        ('y', True),
        ('n', False)
    ]
)
def test_init_skeleton(cookies: Cookies, init_skeleton, has_cmdline):
    """Test use bootstrap"""
    result = cookies.bake(extra_context={'init_skeleton': init_skeleton})

    assert_bake_ok(result)

    exist_cmdline_file = False
    for _, _, files in os.walk(result.project_path):
        for file in files:
            if file == 'cmdline.py':
                exist_cmdline_file = True
    assert exist_cmdline_file == has_cmdline
    assert has_keyword(Path(result.project_path, 'pyproject.toml'), 'cmdline') == has_cmdline
