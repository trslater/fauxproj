from io import StringIO

import pytest


@pytest.fixture
def captured_stdout(monkeypatch):
    buffer = StringIO()

    monkeypatch.setattr("sys.stdout.write", buffer.write)

    return buffer
