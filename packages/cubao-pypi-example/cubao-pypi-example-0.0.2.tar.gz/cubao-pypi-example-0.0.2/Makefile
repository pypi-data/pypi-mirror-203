PROJECT_SOURCE_DIR ?= $(abspath ./)
PROJECT_NAME ?= $(shell basename $(PROJECT_SOURCE_DIR))

all:
	@echo nothing special

lint:
	pre-commit run -a
lint_install:
	pre-commit install

clean:
	rm -rf build dist *.egg-info __pycache__ *.pyc
force_clean:
	docker run --rm -v `pwd`:`pwd` -w `pwd` -it alpine/make make clean
.PHONY: clean force_clean

tox_check:
	python -m tox -e py

data_pull:
	make pull -C data
data_clean:
	make clean -C data

docs_build:
	mkdocs build
docs_serve:
	mkdocs serve -a 0.0.0.0:8088

install:
	python3 -m pip install . --force --user
package:
	python3 -m build
build: package
pypi_remote ?= testpypi
upload:
	python3 -m pip install --upgrade twine
	python3 -m twine upload --repository $(pypi_remote) dist/*
.PHONY: install package build upload

ci:
	python -m tox -e py
.PHONY: ci

test: data_pull pytest clitest
pytest:
	python3 -m pip install pytest
	# pytest --capture=tee-sys tests
	pytest tests -vv
clitest:
	@echo not ready
.PHONY: test pytest clitest

DOCKER_TAG_WINDOWS ?= ghcr.io/cubao/build-env-windows-x64:v0.0.1
DOCKER_TAG_LINUX ?= ghcr.io/cubao/build-env-manylinux2014-x64:v0.0.1
DOCKER_TAG_MACOS ?= ghcr.io/cubao/build-env-macos-arm64:v0.0.1

test_in_win:
	docker run --rm -w `pwd` -v `pwd`:`pwd` -v `pwd`/build/win:`pwd`/build -it $(DOCKER_TAG_WINDOWS) bash
test_in_mac:
	docker run --rm -w `pwd` -v `pwd`:`pwd` -v `pwd`/build/mac:`pwd`/build -it $(DOCKER_TAG_MACOS) bash
test_in_linux:
	docker run --rm -w `pwd` -v `pwd`:`pwd` -v `pwd`/build/linux:`pwd`/build -it $(DOCKER_TAG_LINUX) bash

# https://stackoverflow.com/a/25817631
echo-%  : ; @echo -n $($*)
Echo-%  : ; @echo $($*)
ECHO-%  : ; @echo $* = $($*)
echo-Tab: ; @echo -n '    '
