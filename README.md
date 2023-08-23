# Python Project Sandbox

This is just a place to explore various Python project tools/configurations.

## Installation

```
pip install scalib
```

## Development

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

## Testing

Ensure the dev environment is setup and then run:

```
pytest
```
