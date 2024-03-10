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



@pytest.fixture
def mock_input(monkeypatch):
    """Fixture para la entrada de usuario simulada."""
    user_input = StringIO()
    monkeypatch.setattr('sys.stdin', user_input)
    return user_input

def test_app_menu_command(capfd, monkeypatch):
    """Test que verifica el manejo correcto del comando 'menu'."""
    # Simulamos que el usuario ingresa 'menu' seguido de 'exit'
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()

    # Capturamos la salida de la aplicación
    captured = capfd.readouterr()

    # Verificamos si la aplicación mostró correctamente el menú
    assert "Available commands" in captured.out, "The menu was not displayed as expected"

    # Verificamos si la aplicación salió correctamente
    assert "Exiting..." in captured.out, "The app did not exit as expected"

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
