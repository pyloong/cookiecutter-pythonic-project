"""Post-generate project hooks"""
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(file: str):
    """Remove file"""
    os.remove(os.path.join(PROJECT_DIRECTORY, file))


if __name__ == "__main__":

    if "{{ cookiecutter.use_src_layout|lower }}" != "y":
        shutil.move(
            src=os.path.join(
                PROJECT_DIRECTORY, "src", "{{ cookiecutter.project_slug }}"
            ),
            dst=os.path.join(PROJECT_DIRECTORY),
        )
        shutil.rmtree(os.path.join(PROJECT_DIRECTORY, "src"))

    if "{{ cookiecutter.use_pipenv|lower }}" == "y":
        remove_file("requirements.txt")

    if "{{ cookiecutter.use_pipenv|lower }}" != "y":
        remove_file("Pipfile")

    if "{{ cookiecutter.use_docker|lower }}" != "y":
        remove_file("Dockerfile")
        remove_file(".dockerignore")

    if "{{ cookiecutter.ci_tools|lower }}" != "gitlab":
        remove_file(".gitlab-ci.yml")

    if "{{ cookiecutter.ci_tools|lower }}" != "github":
        shutil.rmtree(os.path.join(PROJECT_DIRECTORY, ".github"), ignore_errors=True)
