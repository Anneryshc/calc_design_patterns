# menu/__init__.py
import os
import sys
import logging  # Agregar logging
from app.commands import CommandHandler
from app.commands import Command

class MenuCommand(Command):
    def execute(self):
        show_menu()

def show_menu():
    command_handler = CommandHandler()

    # Obtener la lista de carpetas en la carpeta 'plugins'
    plugin_folders = [folder for folder in os.listdir('app/plugins') if os.path.isdir(os.path.join('app/plugins', folder))]

    # Registrar el encabezado "Available commands:"
    logging.info("Available commands:")

    # Escribir los comandos del menú en sys.stdout
    for plugin_folder in plugin_folders:
        command = f" - {plugin_folder}"
        sys.stdout.write(command + '\n')
        logging.info(command)