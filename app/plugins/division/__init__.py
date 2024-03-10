from app.commands import Command
import logging

class DivisionCommand(Command):
    """
    A command to perform division of two numbers.
    """

    def execute(self):
        """
        Executes the division command.
        """
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 / num2
            print(f"The division of {num1} and {num2} is : {result}")
        except ValueError:
            logging.error("Invalid input: Please enter valid numbers.")
        except ZeroDivisionError:
            logging.error("Error: Division by zero.")

if __name__ == "__main__":
    DivisionCommand().execute()
    