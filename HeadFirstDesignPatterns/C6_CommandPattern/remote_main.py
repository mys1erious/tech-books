from remote.invokers import RemoteControl
from remote.command import MacroCommand
from remote.receivers.light import Light, LightOnCommand, LightOffCommand
from remote.receivers.ceiling_fan import CeilingFan, CeilingFanHighCommand, CeilingFanMediumCommand, \
    CeilingFanOffCommand
from remote.receivers.garage_door import GarageDoor, GarageDoorOpenCommand, GarageDoorCloseCommand
from remote.receivers.stereo import Stereo, StereoOnWithCDCommand, StereoOff


if __name__ == '__main__':
    remote = RemoteControl()

    light = Light()
    ceiling_fan = CeilingFan('Living Room')
    # garage_door = GarageDoor()
    # stereo = Stereo()

    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)
    ceiling_fan_off = CeilingFanOffCommand(ceiling_fan)
    ceiling_fan_high = CeilingFanHighCommand(ceiling_fan)
    ceiling_fan_medium = CeilingFanMediumCommand(ceiling_fan)
    # garage_open = GarageDoorOpenCommand(garage_door)
    # garage_close = GarageDoorCloseCommand(garage_door)
    # stereo_on = StereoOnWithCDCommand(stereo)
    # stereo_off = StereoOff(stereo)
    party_on = MacroCommand([light_on, ceiling_fan_medium])
    party_off = MacroCommand([light_off, ceiling_fan_off])

    remote.set_command(0, light_on, light_off)
    remote.set_command(1, ceiling_fan_medium, ceiling_fan_off)
    # remote.set_command(2, ceiling_fan_high, ceiling_fan_off)
    # remote.set_command(2, garage_open, garage_close)
    # remote.set_command(3, stereo_on, stereo_off)
    # remote.set_command(3, party_on, party_off)
    remote.set_command(6, party_on, party_on)

    remote.on_button_was_pushed(0)
    remote.off_button_was_pushed(0)
    remote.undo_button_was_pushed()
    remote.on_button_was_pushed(6)
