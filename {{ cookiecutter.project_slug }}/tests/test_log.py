"""Test log"""
import pytest

from {{cookiecutter.project_slug}}.log import update_log_level


@pytest.mark.parametrize(
    ['debug', 'level', 'expect_value'],
    [
        (True, '', 'DEBUG'),
        (True, 'INFO', 'DEBUG'),
        (False, 'DEBUG', 'DEBUG'),
        (False, 'INFO', 'INFO'),
    ]
)
def test_log_level(debug: bool, level: str, expect_value):
    """Test log level"""
    log_level_name = update_log_level(debug, level)
    assert log_level_name == expect_value
