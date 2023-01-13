from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        ...

    @abstractmethod
    def undo(self):
        ...


class NoCommand(Command):
    def execute(self):
        ...

    def undo(self):
        ...


class MacroCommand(Command):
    def __init__(self, commands):
        self.commands = commands

    def execute(self):
        for command in self.commands:
            command.execute()

    def undo(self):
        for command in self.commands:
            command.undo()
