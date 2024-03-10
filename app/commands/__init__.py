from abc import ABC, abstractmethod
import logging
from dotenv import load_dotenv
import os

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.commands = {}
        return cls._instance

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.load_environment_variables()
        self.setup_logging()

    def load_environment_variables(self):
        load_dotenv()

    def setup_logging(self):
        log_level = os.getenv("LOG_LEVEL", "INFO")
        logging.basicConfig(level=log_level)

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, command_name: str):
        try:
            self.logger.info(f"Executing command: {command_name}")
            self.commands[command_name].execute()
        except KeyError:
            self.logger.error(f"No such command: {command_name}")

    def get_available_commands(self):
        return self.commands

