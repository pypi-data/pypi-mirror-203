.ONESHELL:

usage:
	@echo "Usage"
	@echo "	usage (default)"
	@echo "	make setup_venv"
	@echo "	make update_bashrc"
	@echo "	make echo_pass"
	@echo "	make setup_docker_socket"
	@echo "	make freeze"
	@echo "	make install"
	@echo "	make black"
	@echo "	make isort_check"
	@echo "	make isort_apply"
	@echo "	make flake8"
	@echo "	make mypy"
	@echo "	make lint"
	@echo "	make test_unit"
	@echo "	make test_int"
	@echo "	make test_one TEST=<test_name>"
	@echo "	make test_all"
	@echo "	make coverage_unit"
	@echo "	make coverage_xml"
	@echo "	make build"
	@echo "	make deploy_test"

setup_venv:
	@pyenv install --skip-existing 3.10.6 && pyenv local 3.10.6
	@python -m venv venv && . "venv/bin/activate"
	@pip install -e .
	@pip install -e .[dev]
	@pre-commit install

update_bashrc:
	@echo "Please run the following command in your shell:"
	@echo "cp ./.devcontainer/.bashrc ~/.bashrc && source ~/.bashrc"

echo_pass:
	@echo "alskdj"

setup_docker_socket: echo_pass
	@sudo chown python:python /var/run/docker.sock

freeze:
	@pip freeze > requirements.all.txt

install:
	@pip install -e .
	@pip install -e .[dev]

black:
	@python -m black . --check

isort_check:
	@python -m isort . --check-only --diff

isort_apply:
	@python -m isort .

flake8:
	@python -m flake8 .

mypy:
	@python -m mypy .

lint: black isort_check flake8 mypy

test_unit:
	@python -m pytest tests/unit

test_int:
	@python -m pytest tests/integration

test_one:
	@python -m pytest -s -k $(TEST) -vvv

test_all:
	@python -m pytest

coverage_unit:
	@python -m coverage run --source app -m pytest tests/unit
	@python -m coverage report

coverage_xml: coverage_unit
	@python -m coverage xml

load_version:
	@$(eval VERSION := $(shell python -c 'import tomli; print(tomli.load(open("pyproject.toml", "rb"))["project"]["version"])'))

build:
	@rm -rf dist
	@python -m build .

deploy_test: build
	@twine upload dist/* \
		-r testpypi \
		-u __token__ \
		-p $(PYPI_TOKEN_TEST) \
		--non-interactive

deploy_prod: deploy_test
	@twine upload dist/* \
		-u __token__ \
		-p $(PYPI_TOKEN_PROD) \
		--non-interactive