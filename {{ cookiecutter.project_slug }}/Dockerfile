FROM python:{{ cookiecutter.python_version }}

LABEL name="{{ cookiecutter.project_name }}"
LABEL version="{{ cookiecutter.version }}"
LABEL description="{{ cookiecutter.project_description }}"

WORKDIR /app

ADD . ./

RUN ["python"]