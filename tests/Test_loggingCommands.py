"""
Test commands
"""

from io import StringIO
import pytest
from app import App
from app.plugins.addition import DiscordCommand
from app.plugins.subtraction import SubtractionCommand
from app.plugins.multiplication import Multiplicationcommand
from app.plugins.division import DivisionCommand
import logging
from app.plugins.menu import show_menu


@pytest.fixture
def mock_input(monkeypatch):
    """Fixture para la entrada de usuario simulada."""
    user_input = StringIO()
    monkeypatch.setattr('sys.stdin', user_input)
    return user_input

def test_app_menu_command(capsys, caplog):
    # Configurar el logger
    caplog.set_level(logging.INFO)

    # Ejecutar la función show_menu()
    show_menu()

    # Capturar la salida y los registros
    captured = capsys.readouterr()
    logs = caplog.text

    # Verificar si la salida y los registros contienen los comandos esperados
    assert "Available commands:" in logs
    assert " - addition" in captured.out
    assert " - division" in captured.out
    assert " - exit" in captured.out
    assert " - goodbye" in captured.out
    assert " - menu" in captured.out
    assert " - multiplication" in captured.out
    assert " - subtraction" in captured.out

def test_addition_command(capfd, monkeypatch):
    """Test para el comando de suma."""
    # Simulamos que el usuario ingresa dos números
    inputs = iter(['5', '7'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Ejecutamos el comando de suma
    DiscordCommand().execute()

    # Capturamos la salida de la aplicación
    captured = capfd.readouterr()

    # Verificamos si la suma se realizó correctamente y el resultado se imprimió
    assert "The addition of 5.0 and 7.0 is : 12.0\n" in captured.out, "The addition was not done correctly"


def test_subtraction_command_valid_input(capfd, monkeypatch):
    """Test para el comando de resta con entrada válida."""
    # Simulamos que el usuario ingresa dos números
    inputs = iter(['5', '3'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Ejecutamos el comando de resta
    SubtractionCommand().execute()

    # Capturamos la salida de la aplicación
    captured = capfd.readouterr()

    # Verificamos si la resta se realizó correctamente y el resultado se imprimió
    assert "the subtraction 5.0 and 3.0 is : 2.0" in captured.out

def test_subtraction_command_invalid_input(capfd, monkeypatch):
    """Test para el comando de resta con entrada inválida."""
    # Simulamos que el usuario ingresa entradas inválidas
    inputs = iter(['invalid', '3'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Ejecutamos el comando de resta
    SubtractionCommand().execute()

    # Capturamos la salida de la aplicación
    captured = capfd.readouterr()

    # Verificamos si se imprimió el mensaje de error
    assert "Error: Please enter valid numbers." in captured.out

def test_division_command_valid_input(capfd, monkeypatch, mock_input):
    """Test para el comando de división con entrada válida."""
    # Simulamos que el usuario ingresa dos números válidos
    mock_input.write('6\n3\n')
    mock_input.seek(0)

    # Ejecutamos el comando de división
    DivisionCommand().execute()

    # Capturamos la salida de la aplicación
    captured = capfd.readouterr()

    # Verificamos si la división se realizó correctamente y el resultado se imprimió
    assert "the Division 6.0 and 3.0 is : 2.0" in captured.out

def test_division_command_invalid_input(capfd, monkeypatch, mock_input):
    """Test para el comando de división con entrada inválida."""
    # Simulamos que el usuario ingresa una entrada inválida seguida de un número válido
    mock_input.write('invalid\n3\n')
    mock_input.seek(0)

    # Ejecutamos el comando de división
    DivisionCommand().execute()

    # Capturamos la salida de la aplicación
    captured = capfd.readouterr()

    # Verificamos si se imprimió el mensaje de error
    assert "Error: Please enter valid numbers." in captured.out

def test_multiplication_command_invalid_input(capfd, monkeypatch, mock_input):
    """Test para el comando de multiplicación con entrada inválida."""
    # Simulamos que el usuario ingresa un valor inválido seguido de un número válido
    mock_input.write('invalid\n3\n')
    mock_input.seek(0)

    # Ejecutamos el comando de multiplicación
    Multiplicationcommand().execute()

    # Capturamos la salida de la aplicación
    captured = capfd.readouterr()

    # Verificamos si se imprimió el mensaje de error
    assert "Error: Please enter valid numbers." in captured.out
