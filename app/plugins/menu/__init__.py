import sys
# menu/__init__.py
import os 
from app.commands import CommandHandler
from app.commands import Command

class MenuCommand(Command):
    def execute(self):
        show_menu()

def show_menu():
    command_handler = CommandHandler()

    # Obtener la lista de carpetas en la carpeta 'plugins'
    plugin_folders = [folder for folder in os.listdir('app/plugins') if os.path.isdir(os.path.join('app/plugins', folder))]

    print("Available commands:")
    for plugin_folder in plugin_folders:
        print(f" - {plugin_folder}")
