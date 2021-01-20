"""Pre-generate project hooks"""
import re
import sys

MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

MODULE_NAME = "{{ cookiecutter.project_slug}}"

if not re.match(MODULE_REGEX, MODULE_NAME):
    print(
        f"ERROR: The project slug ({MODULE_NAME}) is not a valid Python module name. "
        f"Please do not use a - and use _ instead"
    )

    # Exit to cancel project
    sys.exit(1)
