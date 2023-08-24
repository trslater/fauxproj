from fauxproj import cli


def test_run(monkeypatch, captured_stdout):
    message = "foo"
    monkeypatch.setattr("sys.argv", [None, message])
    
    cli.run()

    assert captured_stdout.getvalue() == f"{message}\n"
