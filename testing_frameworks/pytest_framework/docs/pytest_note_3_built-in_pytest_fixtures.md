##  Built-in pytest fixtures worth learning

- We don't have to create every fixture ourself. 
- Pytest already provides several useful ones.

| Fixture | Purpose |
| --- | --- |
| `tmp_path` | Creates a temporary directory for a test |
| `monkeypatch` | Temporarily modifies attributes, environment variables, or paths |
| `capsys` | Captures output written to standard output and error |
| `request` | Provides information about the requesting test and fixture |
| `pytestconfig` | Gives access to pytest configuration |
