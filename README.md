# cookiecutter-pythonic-project

![GitHub Workflow Status (branch)](https://img.shields.io/github/workflow/status/pyloong/cookiecutter-pythonic-project/main/main?style=flat-square)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/pyloong/cookiecutter-pythonic-project?style=flat-square)
![License](https://img.shields.io/github/license/pyloong/cookiecutter-pythonic-project?style=flat-square)

一个使用 [Cookiecutter](https://github.com/cookiecutter/cookiecutter) 工具生成 Python 工程化项目的模板。

- 文档: [https://pyloong.github.io/cookiecutter-pythonic-project/](https://pyloong.github.io/cookiecutter-pythonic-project/)
- GitHub: [https://github.com/pyloong/cookiecutter-pythonic-project](https://github.com/pyloong/cookiecutter-pythonic-project)

## 特性

- 跨平台支持使用
- 支持自定义配置选项
  
- 默认使用 SRC 项目结构
- 初始化 PEP517 规范打包配置
- 可选初始化通用项目骨架

### 直接使用

```shell
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

```text
❯ cookiecutter https://github.com/pyloong/cookiecutter-pythonic-project
project_name [My Project]:  
project_slug [my_project]: 
project_description [My Awesome Project!]: 
author_name [Author]: 
author_email [author@example.com]: 
version [0.1.0]: 
Select python_version:
1 - 3.7
2 - 3.8
3 - 3.9
Choose from 1, 2, 3 [1]: 
use_src_layout [y]: 
use_pipenv [y]: 
Select index_server:
1 - none
2 - aliyun
Choose from 1, 2 [1]: 
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
- 默认的用户： `Author`
- 默认的邮箱： `author@example.com`
- 默认的版本号： `0.1.0`
- 默认的 Python 版本： `python 3.7`
- 默认的项目结构： SRC 结构
- 默认的 Pypi 索引服务器地址： `https://pypi.org/`
- 默认不使用 Docker 环境
- 默认不适用 CI 环境
- 默认不初始化项目骨架

执行结束后，会在操作命令当前位置生成一个 `my_project` 目录，目录内容如下：

```text
.
├── docs
│         └── development.md
├── LICENSE
├── MANIFEST.in
├── Pipfile
├── pyproject.toml
├── README.md
├── setup.cfg
├── src
│         └── my_project
│             └── __init__.py
├── tests
│         ├── conftest.py
│         ├── __init__.py
│         └── tests.py
└── tox.ini
```

目录中包含了一个完整项目所需要的内容。有项目打包用到的描述文件，记录项目依赖文件和一个简单的测试用例。

项目使用 SRC 目录结构，项目模块在 SRC 下。请尽量测试你的代码，尽早在项目发布之前发现更多可能出现的异常。

## 开发与协作

- fork
- code
- test
- pr
