from app.commands import Command
import logging

class GoodbyeCommand(Command):
    """
    A command to bid farewell.
    """

    def execute(self):
        """
        Executes the goodbye command.
        """
        logging.info("Goodbye")
        print("Goodbye")
