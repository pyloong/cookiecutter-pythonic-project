"""
Configuration center.
Use https://www.dynaconf.com/
"""""
import os
import sys
from pathlib import Path

from dynaconf import Dynaconf


_base_dir = Path(__file__).parent.parent

_settings_files = [
    # All config file will merge.
    Path(__file__).parent / 'settings.yml',  # Load default config.
]

# User configuration. It will be created automatically by the pip installer .
_external_files = [
    Path(sys.prefix, 'etc', '{{ cookiecutter.project_slug }}', 'settings.yml')
]

{%  with %}{% set project_slug_upper = cookiecutter.project_slug|upper() %}
settings = Dynaconf(
    # Set env `{{ project_slug_upper }}_FOO='bar'`，use `settings.FOO` .
    envvar_prefix='{{ project_slug_upper }}',
    settings_files=_settings_files,  # load user configuration.
    # environments=True,  # Enable multi-level configuration，eg: default, development, production
    load_dotenv=True,  # Enable load .env
    # env_switcher='{{ project_slug_upper }}_ENV',
    lowercase_read=False,  # If true, can't use `settings.foo`, but can only use `settings.FOO`
    includes=_external_files,  # Customs settings.
    base_dir=_base_dir,  # `settings.BASEDIR`
)
{% endwith %}