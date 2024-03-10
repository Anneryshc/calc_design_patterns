import sys
from app.commands import Command
import logging

class DiscordCommand(Command):
    """
    A command to perform addition of two numbers.
    """

    def execute(self):
        """
        Executes the addition command.
        """
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 + num2
            print(f"The addition of {num1} and {num2} is : {result}")
        except ValueError:
            logging.error("Invalid input: Please enter valid numbers.")

if __name__ == "__main__":
    DiscordCommand().execute()
    