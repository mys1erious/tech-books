from ..command import Command


class CeilingFan:
    HIGH = 3
    MEDIUM = 2
    LOW = 1
    OFF = 0

    def __init__(self, location):
        self.location = location
        self.speed = self.OFF

    def high(self):
        self.speed = self.HIGH

    def medium(self):
        self.speed = self.MEDIUM

    def low(self):
        self.speed = self.LOW

    def off(self):
        self.speed = self.OFF

    def get_speed(self):
        return self.speed


class CeilingFanHighCommand(Command):
    def __init__(self, ceiling_fan):
        self.ceiling_fan = ceiling_fan
        self.prev_speed = None

    def execute(self):
        self.prev_speed = self.ceiling_fan.get_speed()
        self.ceiling_fan.high()
        print(f'{self.ceiling_fan.location} ceiling fan is on high')

    def undo(self):
        if self.prev_speed == self.ceiling_fan.HIGH:
            self.ceiling_fan.high()
        elif self.prev_speed == self.ceiling_fan.MEDIUM:
            self.ceiling_fan.medium()
            print(f'{self.ceiling_fan.location} ceiling fan is on medium')
        elif self.prev_speed == self.ceiling_fan.LOW:
            self.ceiling_fan.low()
        elif self.prev_speed == self.ceiling_fan.OFF:
            self.ceiling_fan.off()


class CeilingFanMediumCommand(Command):
    def __init__(self, ceiling_fan):
        self.ceiling_fan = ceiling_fan
        self.prev_speed = None

    def execute(self):
        self.prev_speed = self.ceiling_fan.get_speed()
        self.ceiling_fan.medium()
        print(f'{self.ceiling_fan.location} ceiling fan is on medium')

    def undo(self):
        if self.prev_speed == self.ceiling_fan.HIGH:
            self.ceiling_fan.high()
        elif self.prev_speed == self.ceiling_fan.MEDIUM:
            self.ceiling_fan.medium()
            print(f'{self.ceiling_fan.location} ceiling fan is on medium')
        elif self.prev_speed == self.ceiling_fan.LOW:
            self.ceiling_fan.low()
        elif self.prev_speed == self.ceiling_fan.OFF:
            self.ceiling_fan.off()


class CeilingFanOffCommand(Command):
    def __init__(self, ceiling_fan):
        self.ceiling_fan = ceiling_fan
        self.prev_speed = None

    def execute(self):
        self.prev_speed = self.ceiling_fan.get_speed()
        self.ceiling_fan.off()
        print(f'{self.ceiling_fan.location} ceiling fan is off')

    def undo(self):
        if self.prev_speed == self.ceiling_fan.HIGH:
            self.ceiling_fan.high()
        elif self.prev_speed == self.ceiling_fan.MEDIUM:
            self.ceiling_fan.medium()
            print(f'{self.ceiling_fan.location} ceiling fan is on medium')
        elif self.prev_speed == self.ceiling_fan.LOW:
            self.ceiling_fan.low()
        elif self.prev_speed == self.ceiling_fan.OFF:
            self.ceiling_fan.off()
