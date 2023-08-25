.PHONY: build publish dev tox test flake8 mypy

build: tox
	python -m build

bin: tox
	pyinstaller --clean --onefile --name fauxproj cli_wrapper.py

publish: build
	twine upload dist/*

dev:
	pip install -e '.[dev]'

tox:
	tox

test:
	pytest

flake8:
	flake8 src tests

mypy:
	mypy src
