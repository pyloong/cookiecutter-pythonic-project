"""Test config"""
{%- if cookiecutter.init_skeleton == 'y' %}
import pytest
from click.testing import CliRunner


@pytest.fixture()
def clicker():
    """clicker fixture"""
    yield CliRunner()
{%- endif %}
