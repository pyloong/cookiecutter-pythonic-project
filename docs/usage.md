# 使用说明

项目使用 [Cookiecutter](https://github.com/cookiecutter/cookiecutter) 编写，用于自动生成预编写好的项目模板。在使用时，通过交互
输入参数，控制生成逻辑，以达到一定的自定义化，方便更多场景组合使用。使用项目模板生成项目目录，极大程度减少了在项目开始时搭建项目环境的繁琐
步骤，既可以减少编写或复制重复代码，又能避免节省时间。

## 安装依赖

项目模板使用了新的 [PEP-517](https://www.python.org/dev/peps/pep-0517/) 打包规范，所以需要使用更新版本的 pip 。

将 pip 升级到最新版本：

```shell
pip install -U pip
```

安装 [Cookiecutter](https://pypi.org/project/cookiecutter/) :

```shell
pip install -U cookiecutter
```

为了更方便的使用 [Cookiecutter](https://github.com/cookiecutter/cookiecutter) ，推荐在系统环境下或者当前用户环境下安装，而不是
在虚拟环境中安装。

## 生成项目模板

在项目生成目录运行如下命令：

```shell
cookiecutter https://github.com/pyloong/cookiecutter-pythonic-project
```

这是使用 [Cookiecutter](https://github.com/cookiecutter/cookiecutter) 读取放在 Github 上的项目模板。
[Cookiecutter](https://github.com/cookiecutter/cookiecutter) 会首先找到 `cookiecutter.json` 文件，读取其中的
配置，并开启交互提示。

```text
❯ cookiecutter https://github.com/pyloong/cookiecutter-pythonic-project
You've downloaded /home/kevin/.cookiecutters/cookiecutter-pythonic-project before. Is it okay to delete and re-download it? [yes]: 
```

当你不是第一次使用时， [Cookiecutter](https://github.com/cookiecutter/cookiecutter) 可能会提示你要不要更新本地的项目模板。
[Cookiecutter](https://github.com/cookiecutter/cookiecutter) 为了方便本地使用，会在首次运行是将项目模板下载到本地，方便
以后直接读取使用。所以如果仓库代码更新了，你需要先让 [Cookiecutter](https://github.com/cookiecutter/cookiecutter) 更新
最新的项目模板，然后再生成。当然如果你不想使用新功能，也可以跳过更新，继续生成项目。

### 项目名称(project_name)

```text
❯ cookiecutter https://github.com/pyloong/cookiecutter-pythonic-project
You've downloaded /home/kevin/.cookiecutters/cookiecutter-pythonic-project before. Is it okay to delete and re-download it? [yes]: 
project_name [My Project]: Hello World
```

在运行交互时，首先需要输入一个项目名，请输入合法的项目名。

项目名遵循：

- 只能以 `_` 、 `a-z` 和 `A-Z` 开头
- 只能包含 `_` 、 `a-z` 和 `A-Z`
- 输入的前后空格会被删除
- 中间的空格、 `-` 和 `.` 都会被替换成 `_`
- 所有大写字符都会转换成小写字母

即将输入转换成 Python 的蛇形命名法。

### 项目包名称(project_slug)

输入的项目名称会在转换和检查后作为合法的 Python 包名称。

```text
❯ cookiecutter https://github.com/pyloong/cookiecutter-pythonic-project
You've downloaded /home/kevin/.cookiecutters/cookiecutter-pythonic-project before. Is it okay to delete and re-download it? [yes]: 
project_name [My Project]: Hello World
project_slug [hello_world]:
```

可以直接回车使用自动生成的包名称。或者手动输入想要的包名称。

### 项目描述(project_description)

输入项目描述文字，此参数暂时没有显示，你可以输入一段描述项目功能的文字。输入时不能换行，如果使用回车，则会直接进入下一个参数的提示。

```text
❯ cookiecutter https://github.com/pyloong/cookiecutter-pythonic-project
You've downloaded /home/kevin/.cookiecutters/cookiecutter-pythonic-project before. Is it okay to delete and re-download it? [yes]: 
project_name [My Project]: Hello World
project_slug [hello_world]: 
project_description [My Awesome Project!]: This is my first python package, i love it.
```

### 项目作者(author_name)

```text
author_name [Author]: ming
```

### 作者邮箱(author_email)

```text
❯ cookiecutter https://github.com/pyloong/cookiecutter-pythonic-project
You've downloaded /home/kevin/.cookiecutters/cookiecutter-pythonic-project before. Is it okay to delete and re-download it? [yes]: 
project_name [My Project]: Hello World
project_slug [hello_world]: 
project_description [My Awesome Project!]: This is my first python package, i love it.
author_name [Author]: ming
author_email [ming@example.com]: ming@gmail.com
```

### 项目版本(version)

```text
❯ cookiecutter https://github.com/pyloong/cookiecutter-pythonic-project
You've downloaded /home/kevin/.cookiecutters/cookiecutter-pythonic-project before. Is it okay to delete and re-download it? [yes]: 
project_name [My Project]: Hello World
project_slug [hello_world]: 
project_description [My Awesome Project!]: This is my first python package, i love it.
author_name [Author]: ming
author_email [ming@example.com]: ming@gmail.com
version [0.1.0]: 0.1.0
```

输入合法的项目版本号。

[PEP-440](https://www.python.org/dev/peps/pep-0440/) 中规范了符合 Python 规范的版本号。也可以使用较为通用的
[语义化版本 2.0](https://semver.org/lang/zh-CN/) 中规定的版本号写法。

### Python 版本(python_version)

```text
❯ cookiecutter https://github.com/pyloong/cookiecutter-pythonic-project
You've downloaded /home/kevin/.cookiecutters/cookiecutter-pythonic-project before. Is it okay to delete and re-download it? [yes]: 
project_name [My Project]: Hello World
project_slug [hello_world]: 
project_description [My Awesome Project!]: This is my first python package, i love it.
author_name [Author]: ming
author_email [ming@example.com]: ming@gmail.com
version [0.1.0]: 0.1.0    
Select python_version:
1 - 3.7
2 - 3.8
3 - 3.9
Choose from 1, 2, 3 [1]: 
```

选择使用的 Python 版本。默认是 `Python 3.7` 。选择的版本号会出现在打包描述文件 `setup.cfg` 和依赖管理文件 `Pipfile` 文件中。
前者定义使用项目所需要的 Python 版本，后者定义开发时创建的虚拟环境所对应的 Python 版本。

### 使用 SRC 目录结构(use_src_layout)

```text
❯ cookiecutter https://github.com/pyloong/cookiecutter-pythonic-project
You've downloaded /home/kevin/.cookiecutters/cookiecutter-pythonic-project before. Is it okay to delete and re-download it? [yes]: 
project_name [My Project]: Hello World
project_slug [hello_world]: 
project_description [My Awesome Project!]: This is my first python package, i love it.
author_name [Author]: ming
author_email [ming@example.com]: ming@gmail.com
version [0.1.0]: 0.1.0    
Select python_version:
1 - 3.7
2 - 3.8
3 - 3.9
Choose from 1, 2, 3 [1]: 
use_src_layout [y]:
```

选择是否使用 SRC 目录结构。

如果使用 SRC 目录结构，在项目根目录会有一个 `src` 的目录， Python 包在 `src` 下。这种结构方便一个项目包含多个包。

如果不使用 SRC ，则项目的包直接放在项目根目录。

更多关于 Python 目录结构的内容可以阅读[项目结构](https://pyloong.github.io/pythonic-project-guidelines/guidelines/project_structure/)。

### 使用 Pipenv (use_pipenv)

```text
❯ cookiecutter https://github.com/pyloong/cookiecutter-pythonic-project
You've downloaded /home/kevin/.cookiecutters/cookiecutter-pythonic-project before. Is it okay to delete and re-download it? [yes]: 
project_name [My Project]: Hello World
project_slug [hello_world]: 
project_description [My Awesome Project!]: This is my first python package, i love it.
author_name [Author]: ming
author_email [ming@example.com]: ming@gmail.com
version [0.1.0]: 0.1.0    
Select python_version:
1 - 3.7
2 - 3.8
3 - 3.9
Choose from 1, 2, 3 [1]: 
use_src_layout [y]: 
use_pipenv [y]: 
```

选择是否使用 [Pipenv](https://pipenv.pypa.io/en/latest/) 作为虚拟环境管理工具。

使用 Pipenv 的话，会在项目目录自动生成一个 Pipfile 文件，包含了生成的项目所需要的依赖，其中有测试相关的依赖。

如果不使用，则直接生成一个 `requirements.txt` 文件，也会包含所需要的依赖。

注意：如果使用 Pipenv ，需要先安装 Pipenv 。关于 Pipenv 的更多使用技巧，请阅读文档 [Pipenv](https://pipenv.pypa.io/en/latest/) 。

### Python 索引服务器(index_server)

```text
❯ cookiecutter https://github.com/pyloong/cookiecutter-pythonic-project
You've downloaded /home/kevin/.cookiecutters/cookiecutter-pythonic-project before. Is it okay to delete and re-download it? [yes]: 
project_name [My Project]: Hello World
project_slug [hello_world]: 
project_description [My Awesome Project!]: This is my first python package, i love it.
author_name [Author]: ming
author_email [ming@example.com]: ming@gmail.com
version [0.1.0]: 0.1.0    
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
Choose from 1, 2 [1]: 2
```

选择使用的 Python 包索引服务器，默认不选，是使用 [https://pypi.org/](https://pypi.org/) 。提供了一个国内的加速地址
[aliyun](https://mirrors.aliyun.com/pypi/simple/) 。当然你也可以在生成之后修改为自己的内网私服。

如果上一步你选择了使用 Pipenv ，则需要修改 `Pipfile` 文件，如果不使用 Pipenv ，则修改 `requirements.txt` 文件即可。

### 使用 Docker(use_docker)

```text
❯ cookiecutter https://github.com/pyloong/cookiecutter-pythonic-project
You've downloaded /home/kevin/.cookiecutters/cookiecutter-pythonic-project before. Is it okay to delete and re-download it? [yes]: 
project_name [My Project]: Hello World
project_slug [hello_world]: 
project_description [My Awesome Project!]: This is my first python package, i love it.
author_name [Author]: ming
author_email [ming@example.com]: ming@gmail.com
version [0.1.0]: 0.1.0    
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
Choose from 1, 2 [1]: 2
use_docker [n]: 
```

选择是否使用 Docker 。默认不使用。

如果选择使用，会在项目中生成简单的 `Dockerfile` 和 `.dockerignoer` 文件。

### CI 工具(ci_tools)

```text
❯ cookiecutter https://github.com/pyloong/cookiecutter-pythonic-project
You've downloaded /home/kevin/.cookiecutters/cookiecutter-pythonic-project before. Is it okay to delete and re-download it? [yes]: 
project_name [My Project]: Hello World
project_slug [hello_world]: 
project_description [My Awesome Project!]: This is my first python package, i love it.
author_name [Author]: ming
author_email [ming@example.com]: ming@gmail.com
version [0.1.0]: 0.1.0    
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
Choose from 1, 2 [1]: 2
use_docker [n]: 
Select ci_tools:
1 - none
2 - Gitlab
3 - Github
Choose from 1, 2, 3 [1]: 3
```

选择使用的 CI 工具，可选的有 `Gitlab` 和 `Github` 。如果选择一个 CI 工具，默认会生成项目的测试、构建、发布到索引服务器的三步操作。

### 初始化项目骨架(init_skeleton)

```text
❯ cookiecutter https://github.com/pyloong/cookiecutter-pythonic-project
You've downloaded /home/kevin/.cookiecutters/cookiecutter-pythonic-project before. Is it okay to delete and re-download it? [yes]: 
project_name [My Project]: Hello World
project_slug [hello_world]: 
project_description [My Awesome Project!]: This is my first python package, i love it.
author_name [Author]: ming
author_email [ming@example.com]: ming@gmail.com
version [0.1.0]: 0.1.0    
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
Choose from 1, 2 [1]: 2
use_docker [n]: 
Select ci_tools:
1 - none
2 - Gitlab
3 - Github
Choose from 1, 2, 3 [1]: 3
init_skeleton [n]:
```

选择是否初始化项目骨架。如果选择初始化，则会在生成的项目中增加配置系统，初始化日志配置，提供一个通用的命令行入口，并将
命令行入口注册到打包描述文件 `setup.cfg` 中。同时附带对应的测试代码。

## 使用生成后的项目

当上面的所有步骤操作完成后，就会在当前目录生成一个 Python 项目，其目录结构如下：

```text
hello_world
├── docs
│         └── development.md
├── LICENSE
├── MANIFEST.in
├── Pipfile
├── pyproject.toml
├── README.md
├── setup.cfg
├── src
│         └── hello_world
│             └── __init__.py
├── tests
│         ├── conftest.py
│         ├── __init__.py
│         └── tests.py
└── tox.ini
```

在项目根目录，包含了一些描述性的文件：

- `LICENSE` ： 项目的许可证
- `MANIFEST.in` ：描述项目打包是要包含的目录和文件
- `Pipfile` ：Pipenv 所使用的依赖描述文件
- `pyproject.toml` ：符合 [PEP-517](https://www.python.org/dev/peps/pep-0517/) 规范的项目打包描述文件
- `README.md` ：项目自述文件
- `setup.cfg` ：项目打包是使用的后端工具 setuptools 的配置文件。
- `tox.ini` ：自动化测试工具 [Tox](https://tox.readthedocs.io/en/latest/) 的配置文件。

还有一些目录：

- `docs` ：文档目录，用来记录开发和使用时的文档
- `src` ：使用了 SRC 目录结构生成目录，用来放置项目的包
- `tests` ：测试目录，用来放置对 `src` 下面的包做测试的目录。

直接运行 `tox` 检查项目状态：

```text
❯ tox
.package create: /tmp/test/hello_world/.tox/.package
.package installdeps: setuptools, wheel
py37 create: /tmp/test/hello_world/.tox/py37
py37 installdeps: pipenv
py37 inst: /tmp/test/hello_world/.tox/.tmp/package/1/hello_world-0.1.0.tar.gz
py37 installed: appdirs==1.4.4,certifi==2021.5.30,distlib==0.3.2,filelock==3.0.12,hello-world @ file:///tmp/test/hello_world/.tox/.tmp/package/1/hello_world-0.1.0.tar.gz,importlib-metadata==4.5.0,pipenv==2021.5.29,six==1.16.0,typing-extensions==3.10.0.0,virtualenv==20.4.7,virtualenv-clone==0.5.4,zipp==3.4.1
py37 run-test-pre: PYTHONHASHSEED='290397051'
py37 run-test: commands[0] | pipenv install -d
Courtesy Notice: Pipenv found itself running within a virtual environment, so it will automatically use that environment, instead of creating its own for any project. You can set PIPENV_IGNORE_VIRTUALENVS=1 to force pipenv to ignore that environment and create its own instead. You can set PIPENV_VERBOSITY=-1 to suppress this warning.
Pipfile.lock not found, creating...
Locking [dev-packages] dependencies...
Building requirements...
Resolving dependencies...
✔ Success! 
Locking [packages] dependencies...
Updated Pipfile.lock (8c4ae8)!
Installing dependencies from Pipfile.lock (8c4ae8)...
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 18/18 — 00:00:02
py37 run-test: commands[1] | pytest
=========================================================================== test session starts ===========================================================================
platform linux -- Python 3.7.3, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
cachedir: .tox/py37/.pytest_cache
rootdir: /tmp/test/hello_world, configfile: setup.cfg, testpaths: tests
plugins: cov-2.12.1
collected 1 item                                                                                                                                                          

tests/tests.py .                                                                                                                                                    [100%]

============================================================================ 1 passed in 0.01s ============================================================================
isort create: /tmp/test/hello_world/.tox/isort
isort installdeps: isort
isort inst: /tmp/test/hello_world/.tox/.tmp/package/1/hello_world-0.1.0.tar.gz
isort installed: hello-world @ file:///tmp/test/hello_world/.tox/.tmp/package/1/hello_world-0.1.0.tar.gz,isort==5.8.0
isort run-test-pre: PYTHONHASHSEED='290397051'
isort run-test: commands[0] | isort . --check-only --diff
Skipped 1 files
pylint create: /tmp/test/hello_world/.tox/pylint
pylint installdeps: pipenv
pylint inst: /tmp/test/hello_world/.tox/.tmp/package/1/hello_world-0.1.0.tar.gz
pylint installed: appdirs==1.4.4,certifi==2021.5.30,distlib==0.3.2,filelock==3.0.12,hello-world @ file:///tmp/test/hello_world/.tox/.tmp/package/1/hello_world-0.1.0.tar.gz,importlib-metadata==4.5.0,pipenv==2021.5.29,six==1.16.0,typing-extensions==3.10.0.0,virtualenv==20.4.7,virtualenv-clone==0.5.4,zipp==3.4.1
pylint run-test-pre: PYTHONHASHSEED='290397051'
pylint run-test: commands[0] | pipenv install -d
Courtesy Notice: Pipenv found itself running within a virtual environment, so it will automatically use that environment, instead of creating its own for any project. You can set PIPENV_IGNORE_VIRTUALENVS=1 to force pipenv to ignore that environment and create its own instead. You can set PIPENV_VERBOSITY=-1 to suppress this warning.
Installing dependencies from Pipfile.lock (8c4ae8)...
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 18/18 — 00:00:02
pylint run-test: commands[1] | pylint tests src

-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 7.25/10, +2.75)

_________________________________________________________________________________ summary _________________________________________________________________________________
  py37: commands succeeded
  isort: commands succeeded                                                                                                                                                
  pylint: commands succeeded                                                                                                                                               
  congratulations :)                                                                                                                                                       
```

运行 `tox` 进行自动化测试，可以看到自动执行了 `py37` 的测试，
[isort](https://pycqa.github.io/isort/) 的包导入检查，
[pylint](https://www.pylint.org/) 的 Python 语法规范检查。

当所有检查都正常时， Tox 的自动化逻辑才会正常通过，否则会报出异常，此时你需要根据提示调整代码，并再次运行，直到全部通过。

如果你讨厌这些繁琐的检查，也可以修改 `tox.ini` 文件，删除不喜欢的配置，或者不运行 `tox` 。但是并不推荐你这么做。因为良好的编码习惯
是一个优秀的开发人员最基本的要求。
