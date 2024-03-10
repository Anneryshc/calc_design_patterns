import pkgutil
import importlib
from app.commands import CommandHandler
from app.commands import Command
from app.plugins.menu import MenuCommand
import logging
from dotenv import load_dotenv
import os

class App:
    def __init__(self):
        self.command_handler = CommandHandler()
        self.is_running = True
        self.user_input = None  # Inicializar la entrada del usuario

        # Configurar loggings
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

        # Cargar variables de entorno desde el archivo .env
        load_dotenv()

    def load_plugins(self):
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, Command):
                            self.command_handler.register_command(plugin_name, item())
                    except TypeError:
                        continue

        # Registra el comando de menú
        self.command_handler.register_command('menu', MenuCommand())

    def start(self):
        self.load_plugins()
        print("Type 'exit' to exit.")
        while self.is_running:
            if self.user_input is not None:
                user_input = self.user_input  # Utilizar la entrada proporcionada
                self.user_input = None  # Restablecer la entrada para la próxima iteración
            else:
                user_input = input(">>> ").strip()
            if user_input == 'exit':
                self.logger.info("Exiting...")
                raise SystemExit  # Lanzar excepción SystemExit
            else:
                self.command_handler.execute_command(user_input)

if __name__ == "__main__":
    app = App()
    app.start()
