import sys
from app.commands import Command


class Multiplicationcommand (Command):
    def execute(self):
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 * num2
            print(f"the subtraction {num1} and {num2} is : {result}")
        except ValueError:
            print("Error: Please enter valid numbers.")

# Llama a la función para ejecutarla directamente al importar el módulo
if __name__ == "__main__":
    Multiplicationcommand().execute()
    