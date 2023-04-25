# cookiecutter-pythonic-project

![GitHub Workflow Status (branch)](https://img.shields.io/github/actions/workflow/status/pyloong/cookiecutter-pythonic-project/main.yml?style=flat-square)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/pyloong/cookiecutter-pythonic-project?style=flat-square)
![License](https://img.shields.io/github/license/pyloong/cookiecutter-pythonic-project?style=flat-square)
![support python version](https://img.shields.io/badge/python-3.10%20%7C%203.11-blue)

一个使用 [Cookiecutter](https://github.com/cookiecutter/cookiecutter) 工具生成 Python 工程化项目的模板。

- 文档: [https://pyloong.github.io/cookiecutter-pythonic-project/](https://pyloong.github.io/cookiecutter-pythonic-project/)
- GitHub: [https://github.com/pyloong/cookiecutter-pythonic-project](https://github.com/pyloong/cookiecutter-pythonic-project)

## 特性

- 跨平台支持使用
- 支持自定义配置选项
- 默认使用 SRC 项目结构
- 初始化 PEP517 规范打包配置，默认使用 [poetry](https://python-poetry.org/) 打包。
- 可选初始化通用项目骨架

**注意：** 项目支持 `Python >= 3.10` , 并且已经启用 `Python 3.11` 相关功能和稳定性测试。

### 直接使用

```bash
# 升级最新 pip
pip install -U pip

# 安装或升级 cookiecutter
pip install -U cookiecutter

# 使用 cookiecutter 加载项目模板，生成项目
# 回车运行的时候，需要根据提示交互选择启用的功能。
# 如果使用默认配置，则一路回车就可以。
cookiecutter https://github.com/pyloong/cookiecutter-pythonic-project
```

### 详细说明

#### 创建项目

```text
❯ cookiecutter https://github.com/pyloong/cookiecutter-pythonic-project
project_name [My Project]: 
project_slug [my_project]: 
project_description [My Awesome Project!]: 
author_name [Author]: 
author_email [author@example.com]: 
version [0.1.0]: 
Select python_version:
1 - 3.11
2 - 3.10
Choose from 1, 2 [1]: 2
use_src_layout [y]: 
use_poetry [y]: 
use_docker [n]: 
Select ci_tools:
1 - none
2 - Gitlab
3 - Github
Choose from 1, 2, 3 [1]: 
init_skeleton [n]: 
```

上述操作，全部使用了默认逻辑：

- 使用默认项目名： `My Project`
- 默认的项目目录和包名： `my_project`
- 默认的项目描述： `My Awesome Project!`
- 默认的用户： `author`
- 默认的邮箱： `author@example.com`
- 默认的版本号： `0.1.0`
- 默认的 Python 版本： `python 3.10`
- 默认的项目结构： SRC 结构
- 默认不使用 Docker 环境
- 默认不适用 CI 环境
- 默认不初始化项目骨架

执行结束后，会在操作命令当前位置生成一个 `my_project` 目录，目录内容如下：

```text
my_project
├── LICENSE
├── README.md
├── docs
│   └── development.md
├── pyproject.toml
├── .editorconfig
├── .pre-commit-config.yaml
├── src
│   └── my_project
│       └── __init__.py
├── tests
│   ├── __init__.py
│   ├── conftest.py
│   └── test_version.py
└── tox.ini
```

目录中包含了一个完整项目所需要的内容。有项目打包用到的描述文件，记录项目依赖文件和一个简单的测试用例。

项目使用 SRC 目录结构，项目模块在 SRC 下。强烈建议开发前测试你的代码，可以避免因项目生成项目模板导致后期开发异常。

#### 使用项目

进入项目目录：

```bash
## 进入到项目中
cd my_project

## 初始化项目环境
## 如果使用了 poetry 则执行 poetry install -v 
poetry install -v

## 如果不使用 poetry 则执行 pip install -r requirements.txt
## 强烈建议使用 virtualenv 虚拟环境管理项目环境
## 安装 virtualenv 虚拟环境管理工具
# pip install virtualenv
## 使用 virtualenv 创建虚拟环境
# virtualenv .venv
## 进入虚拟环境中
# source .venv/bin/activate
## 安装项目必要依赖
# pip install -r requirements.txt
## 后续安装依赖直接使用 pip install aiohttp 即可
## 可以使用 pip freeze 生成当前依赖版本，并更新依赖
# pip freeze > requirements.txt

## 进入虚拟环境
poetry shell

## 自动化测试项目
tox

## 安装项目开发时需要的依赖。安装完成后，会自动更新 poetry.lock 文件，锁定当前版本。
poetry add aiohttp

## pre-commit预提交，是git hooks中的一个钩子，由 git commit 命令调用，可以通过 --no-verify 参数绕过调用 pre-commit 。
## 要使用pre-commit钩子，请先安装pre-commit库
pip install pre-commit
## 命令行安装，卸载为 `pre-commit uninstall`
pre-commit install
## git commit -m '修改内容' 会触发预提交钩子指令，完成校验逻辑
```

更多使用细节请查看 [使用说明](./docs/usage.md) 。

## 开发与协作

- fork
- code
- test
- pr
