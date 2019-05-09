# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}


## Features
* TODO fill features

## Installation
Create virtualenv if you want and then just run `make install`.

## Requirements
First, there are [templates](requirements/base) of requirements files - that's the place where you want to add new dependencies (might be with version range, eg. `flask>=1.0<1.1`). These templates are compiled to concrete requirements.

[Concrete requirements](requirements/concrete) have frozen versions of project dependencies and their sub-dependencies. They're used mostly in two places: [Dockerfile](Dockerfile) and [setup.py](setup.py).

## Project management
Actions in project are managed with [GNU Make](https://www.gnu.org/software/make/). If you want to check them, read the [Makefile](Makefile). 

## Tests
Tests are managed with [py.test](https://docs.pytest.org/en/latest/). If you want to run them just `make tests`.

## Linters
There's bunch of linters configured in project:
  * [flake8](https://flake8.pycqa.org/en/latest/)
  * [mypy](https://mypy.readthedocs.io/en/latest/)
  * [isort](https://isort.readthedocs.io/en/latest/)
  * [bandit](https://bandit.readthedocs.io/en/latest/)

Their configuration is held in [setup.cfg](setup.cfg). You can run each of them using make - like `make flake8` etc., or all of them at once with `make linters`. Moreover, there is autofix command for isort, `make isort_fix`. 
