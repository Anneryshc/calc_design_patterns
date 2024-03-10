import sys
import os
import logging
from app.commands import Command
from dotenv import load_dotenv

class MultiplicationCommand(Command):
    def __init__(self):
        super().__init__()
        # Configurar el logger
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        # Crear un formateador de registro
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        # Crear un manejador de archivo para guardar los registros
        file_handler = logging.FileHandler('multiplication.log')
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def execute(self):
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 * num2
            print(f"The multiplication of {num1} and {num2} is : {result}")
            self.logger.info(f"The multiplication of {num1} and {num2} is : {result}")
        except ValueError:
            print("Error: Please enter valid numbers.")
            self.logger.error("Error: Please enter valid numbers.")

# Llama a la función para ejecutarla directamente al importar el módulo
if __name__ == "__main__":
    # Configurar logging
    logging.basicConfig(level=logging.INFO)

    # Cargar variables de entorno desde el archivo .env
    load_dotenv()

    # Obtener la ubicación de la carpeta de plugins desde la variable de entorno
    plugins_folder = os.getenv("PLUGINS_FOLDER", "app/plugins")

    # Ejecutar el comando de multiplicación
    MultiplicationCommand().execute()

    