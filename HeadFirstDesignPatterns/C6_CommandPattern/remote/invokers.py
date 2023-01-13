from .command import NoCommand


class SimpleRemoteControl:
    def __init__(self):
        self.slot = None

    def set_command(self, command):
        self.slot = command

    def button_was_pressed(self):
        self.slot.execute()


class RemoteControl:
    def __init__(self):
        self.on_commands = []
        self.off_commands = []

        no_command = NoCommand()
        for i in range(7):
            self.on_commands.append(no_command)
            self.off_commands.append(no_command)
        self.undo_command = no_command

    def set_command(self, slot, on_command, off_command):
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command

    def on_button_was_pushed(self, slot):
        self.on_commands[slot].execute()
        self.undo_command = self.on_commands[slot]

    def off_button_was_pushed(self, slot):
        self.off_commands[slot].execute()
        self.undo_command = self.off_commands[slot]

    def undo_button_was_pushed(self):
        self.undo_command.undo()

    def __str__(self):
        s = '\n------ Remote Control ------\n'
        for i in range(len(self.on_commands)):
            s += f'[slot {i}] {type(self.on_commands[i]).__name__}    {type(self.off_commands[i]).__name__}\n'
        s += f'[slot undo] {type(self.undo_command).__name__}\n'
        return s
