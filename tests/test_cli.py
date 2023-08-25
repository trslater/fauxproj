from fauxproj import cli


def test_run(monkeypatch, captured_stdout):
    N = 2
    monkeypatch.setattr("sys.argv", [None, N])
    
    cli.run()

    assert captured_stdout.getvalue() == "1.4142135623730951\n"
