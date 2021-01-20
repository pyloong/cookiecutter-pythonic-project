"""Tests"""
from {{cookiecutter.project_slug}} import __version__


def test_version():
    """Test version"""
    assert __version__ == '{{ cookiecutter.version }}'
