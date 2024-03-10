from app.commands import Command
from app.commands import CommandHandler
import os
import dotenv

class MenuCommand(Command):
    """
    A command to display the available menu options.
    """

    def execute(self):
        """
        Executes the menu command to display available options.
        """
        show_menu()

def show_menu():
    """
    Displays the menu with available commands.
    """
    # Cargar variables de entorno desde el archivo .env
    dotenv.load_dotenv()

    # Obtener la ubicación de la carpeta de plugins desde la variable de entorno
    plugins_folder = os.getenv('PLUGINS_FOLDER', 'app/plugins')

    command_handler = CommandHandler()

    # Obtener la lista de carpetas en la carpeta de plugins
    plugin_folders = [folder for folder in os.listdir(plugins_folder) if os.path.isdir(os.path.join(plugins_folder, folder))]

    print("Available commands:")
    for plugin_folder in plugin_folders:
        print(f" - {plugin_folder}")
