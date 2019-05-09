# Cookiecutter Python Package

Cookiecutter template for a Python package.

## Features

* Testing setup with pytest
* Linters set up:
  * flake8
  * mypy
  * isort
  * bandit
* Easy invocation of commands with make
* Ready for GitLab CI
* Automatic git repo init & initial commit
* SCM versioning
* Base Dockerfile
* Package managed with setup.py
* Compilable requirements used in setup.py and Dockerfile

## Quickstart

Install Cookiecutter:

    pip install -U cookiecutter

Generate a Python package project:

    cookiecutter https://gitlab.com/andrzej3393/cookiecutter_python_package.git
