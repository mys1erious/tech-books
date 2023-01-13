from ..command import Command


class Stereo:
    def __init__(self):
        self.volume = 0

    def on(self):
        print('Stereo is On')

    def off(self):
        print('Stereo is Off')

    def set_cd(self):
        print('Stereo is set to CD')

    def set_dvd(self):
        print('Stereo is set to DVD')

    def set_radio(self):
        print('Stereo is set to Radio')

    def set_volume(self, volume):
        self.volume = volume
        print(f'Stereo volume is set to {self.volume}')


class StereoOnWithCDCommand(Command):
    def __init__(self, stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.on()
        self.stereo.set_cd()
        self.stereo.set_volume(11)


class StereoOff(Command):
    def __init__(self, stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.off()
