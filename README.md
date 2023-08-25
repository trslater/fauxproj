# Python Project Sandbox

This is just a place to explore various Python project tools/configurations.

> :warning: This is a fake project **do not install**

## Installation

```
pip install fauxproj
```

## Usage

```
fauxproj MESSAGE
```

Prints `MESSAGE` to terminal.

## Development

If you have make installed, please use included `Makefile` as it streamlines running these operations.

### Environment

I recommend using `venv` first:

```
python -m venv venv
```

Then install the library in editable mode with the `dev` extras:

```
pip install -e .[dev]
```

You may need to quote `.[dev]` in certain shells:

```
pip install -e '.[dev]'
```

### Testing

To just run tests on local dev environment:

```
pytest
```

For full tests:

```
tox
```

### Publishing

```
python -m build
twine upload dist/*
```

You can publish to the testing PyPI to make sure everything works how you want it:

```
twine upload -r testpypi dist/*
```

## References

-   A lot of the configuration/basic setup is based on [mCoding's](https://mcoding.io) great [video tutorial](https://www.youtube.com/watch?v=DhUpxWjOhME).
