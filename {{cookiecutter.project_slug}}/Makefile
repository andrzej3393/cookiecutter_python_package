.PHONY: clean
clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

.PHONY: clean-build
clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

.PHONY: clean-pyc
clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

.PHONY: clean-test
clean-test: ## remove test and coverage artifacts
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache


.PHONY: linters
linters: flake8 mypy isort bandit ## check style

.PHONY: flake8
flake8: ## check codebase with flake8
	flake8 {{ cookiecutter.project_slug }} tests

.PHONY: mypy
mypy: ## check typehints
	mypy {{ cookiecutter.project_slug }} tests

.PHONY: isort
isort: ## check if imports are sorted correctly
	isort -rc -c {{ cookiecutter.project_slug }} tests

.PHONY: isort_fix
isort_fix: ## fix imports
	isort -rc {{ cookiecutter.project_slug }} tests

.PHONY: bandit
bandit: ## check if there aren't any secrets in code
	bandit -r {{ cookiecutter.project_slug }}


.PHONY: tests
tests: ## run tests quickly with the default Python
	pytest


REQUIREMENTS_BASENAMES = requirements requirements.test requirements.setup
REQUIREMENTS_ENVS = CUSTOM_COMPILE_COMMAND="make requirements"
REQUIREMENTS_CMD = pip-compile -o requirements/concrete/$(name).txt requirements/base/$(name).in

.PHONY: requirements
requirements: ## compile all the requirements files
	mkdir -p requirements/concrete
	$(foreach name,$(REQUIREMENTS_BASENAMES),$(REQUIREMENTS_ENVS) $(REQUIREMENTS_CMD);)


.PHONY: release
release: dist ## package and upload a release
	twine upload dist/*

.PHONY: dist
dist: clean ## builds source and wheel package
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist


.PHONY: install
install: clean ## install the package to the active Python's site-packages
	pip install -e .[testing]
