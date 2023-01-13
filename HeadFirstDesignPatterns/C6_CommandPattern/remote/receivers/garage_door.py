from ..command import Command


class GarageDoor:
    def up(self):
        print('Garage Door is Open')

    def down(self):
        print('Garage Door is Closed')

    def stop(self):
        print('Garage Door Stopped')

    def light_on(self):
        print('Garage light is turned on')

    def light_off(self):
        print('Garage light is turned off')


class GarageDoorOpenCommand(Command):
    def __init__(self, garage_door):
        self.garage_door = garage_door

    def execute(self):
        self.garage_door.up()
        self.garage_door.light_on()


class GarageDoorCloseCommand(Command):
    def __init__(self, garage_door):
        self.garage_door = garage_door

    def execute(self):
        self.garage_door.down()
        self.garage_door.light_off()
