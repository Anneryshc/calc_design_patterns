"""
Test de comandos.
"""

import logging
import pytest
from app import App

@pytest.fixture
def app():
    """Fixture para instanciar la aplicación."""
    return App()

def test_app_start_exit_command(app, monkeypatch, caplog):
    """Test que verifica que la aplicación inicie y salga correctamente."""
    # Configura el nivel de logging para capturar registros
    caplog.set_level(logging.INFO)

    # Simula que el usuario ingresa 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    # Ejecuta la aplicación y verifica que se lance la excepción SystemExit
    with pytest.raises(SystemExit):
        app.start()

    # Captura los registros generados durante la ejecución
    logs = caplog.text
    # Verifica si la salida y los registros contienen el mensaje de salida esperado
    assert "Exiting..." in logs
