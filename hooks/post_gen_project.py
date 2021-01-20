"""Post-generate project hooks"""
import os
import shutil
from pathlib import Path


def remove_file(file: str, *files):
    """
    Remove file
    :param file:
    :param files:
    :return:
    """
    os.remove(file)
    for _f in files:
        os.remove(_f)


def setup_src_layout(flag: str):
    """Setup src layout"""
    if flag != 'y':
        # shutil.move can not pass Path, will raise Exception.
        shutil.move(src=str(Path('src', PROJECT_SLUG)), dst='.')
        shutil.rmtree('src')


def setup_pipenv(flag: str):
    """
    Setup pipenv.
    If n, use requirements.txt
    :param flag:
    :return:
    """
    if flag != 'y':
        remove_file("Pipfile")
    else:
        remove_file("requirements.txt")


def setup_docker(flag: str):
    """
    Setup docker.
    :param flag:
    :return:
    """
    if flag != 'y':
        remove_file('Dockerfile', '.dockerignore')


def setup_ci_tools(flag: str):
    """
    Setup ci tools
    :param flag:
    :return:
    """
    if flag != 'gitlab':
        remove_file('.gitlab-ci.yml')
    if flag != 'github':
        shutil.rmtree('.github', ignore_errors=True)


def setup_bootstrap(flag: str):
    """
    Setup bootstrap
    If flag == y , keep bootstrap.
    :param flag:
    :return:
    """
    test_path = Path('tests')
    src_path = Path(PROJECT_SLUG)
    if SRC_LAYOUT == 'y':
        src_path = Path('src', PROJECT_SLUG)
    if flag != 'y':
        shutil.rmtree(src_path / 'config')
        remove_file(
            src_path / 'cmdline.py',
            src_path / 'log.py',
            test_path / 'test_cmdline.py',
            test_path / 'test_log.py'
        )


if __name__ == "__main__":
    PROJECT_SLUG = '{{ cookiecutter.project_slug }}'
    SRC_LAYOUT = '{{ cookiecutter.use_src_layout|lower }}'
    USE_PIPENV = '{{ cookiecutter.use_pipenv|lower }}'
    USE_DOCKER = '{{ cookiecutter.use_docker|lower }}'
    CI_TOOLS = '{{ cookiecutter.ci_tools|lower }}'
    INIT_BOOTSTRAP = '{{ cookiecutter.init_bootstrap|lower }}'

    setup_src_layout(SRC_LAYOUT)
    setup_pipenv(USE_PIPENV)
    setup_docker(USE_DOCKER)
    setup_ci_tools(CI_TOOLS)
    setup_bootstrap(INIT_BOOTSTRAP)
