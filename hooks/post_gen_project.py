"""Post-generate project hooks"""
import os
import shutil
from pathlib import Path


def remove_file(file: Path, *files: Path):
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


def setup_poetry(flag: str):
    """
    Setup poetry.
    If n, use requirements.txt, and require `setup.cfg` file
    else remove `requirements.txt` and `setup.cfg`.
    :param flag:
    :return:
    """
    if flag != 'y':
        pass
    else:
        remove_file(Path('requirements.txt'), Path('setup.cfg'), Path('MANIFEST.in'))


def setup_docker(flag: str):
    """
    Setup docker.
    :param flag:
    :return:
    """
    if flag != 'y':
        remove_file(Path('Dockerfile'), Path('.dockerignore'))


def setup_ci_tools(flag: str):
    """
    Setup ci tools
    :param flag:
    :return:
    """
    if flag != 'gitlab':
        remove_file(Path('.gitlab-ci.yml'))
    if flag != 'github':
        shutil.rmtree('.github', ignore_errors=True)


def setup_skeleton(flag: str):
    """
    Setup skeleton
    If flag == y , keep skeleton.
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
            test_path / 'test_log.py',
        )


if __name__ == "__main__":
    PROJECT_SLUG = '{{ cookiecutter.project_slug }}'
    SRC_LAYOUT = '{{ cookiecutter.use_src_layout|lower }}'
    USE_POETRY = '{{ cookiecutter.use_poetry|lower }}'
    USE_DOCKER = '{{ cookiecutter.use_docker|lower }}'
    CI_TOOLS = '{{ cookiecutter.ci_tools|lower }}'
    INIT_SKELETON = '{{ cookiecutter.init_skeleton|lower }}'

    setup_src_layout(SRC_LAYOUT)
    setup_poetry(USE_POETRY)
    setup_docker(USE_DOCKER)
    setup_ci_tools(CI_TOOLS)
    setup_skeleton(INIT_SKELETON)
