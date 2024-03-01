import sys
from app.commands import Command


class DiscordCommand(Command):
    def execute(self):
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            result = num1 + num2
            print(f"La suma de {num1} y {num2} es: {result}")
        except ValueError:
            print("Error: Por favor ingrese números válidos.")

# Llama a la función para ejecutarla directamente al importar el módulo
if __name__ == "__main__":
    DiscordCommand().execute()