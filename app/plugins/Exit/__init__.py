from app.commands import Command
import sys
import logging

class ExitCommand(Command):
    """
    A command to exit the program.
    """

    def execute(self):
        """
        Executes the exit command.
        """
        logging.info("Exiting...")
        sys.exit()
        