"""
Module docstring: Test commands
"""

import pytest
from app import App

@pytest.fixture
def app():
    """Fixture para instanciar la aplicación."""
    return App()

def test_app_start_exit_command(app, monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    # Simulate user entering 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    with pytest.raises(SystemExit):
        app.start()
