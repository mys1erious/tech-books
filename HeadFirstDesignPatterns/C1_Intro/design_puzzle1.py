# Each character can make use of one weapon at a time, but can
#   change weapons at any time during the game.
# 1. Arrange the classes.
# 2. Identify one abstract class, one interface, and eight classes.
# 3. Put the method setWeapon() into the right class.
from abc import ABC, abstractmethod


class Character(ABC):
    weapon = None

    def fight(self):
        if self.weapon:
            self.weapon.use_weapon()
        else:
            print(f'{type(self).__name__} doesnt have a weapon to fight')

    def set_weapon(self, w):
        self.weapon = w


class Queen(Character):
    def __init__(self):
        self.weapon = BowAndArrowBehavior()

    def fight(self):
        print('Queen fights')
        super().fight()


class King(Character):
    def __init__(self):
        self.weapon = KnifeBehavior()

    def fight(self):
        print('King fights')
        super().fight()


class Troll(Character):
    def __init__(self):
        self.weapon = AxeBehavior()

    def fight(self):
        print('Troll fights')
        super().fight()


class Knight(Character):
    def __init__(self):
        self.weapon = SwordBehavior()

    def fight(self):
        print('Knight fights')
        super().fight()


class WeaponBehavior(ABC):
    @abstractmethod
    def use_weapon(self):
        ...


class KnifeBehavior(WeaponBehavior):
    def use_weapon(self):
        print('Cutting with a knife')


class BowAndArrowBehavior(WeaponBehavior):
    def use_weapon(self):
        print('Shooting an arrow with a bow')


class AxeBehavior(WeaponBehavior):
    def use_weapon(self):
        print('Chopping with an axe')


class SwordBehavior(WeaponBehavior):
    def use_weapon(self):
        print('Swinging with a sword')


if __name__ == '__main__':
    knight = Knight()
    knight.fight()
    knight.set_weapon(AxeBehavior())
    knight.fight()

    queen = Queen()
    queen.fight()
    queen.set_weapon(None)
    queen.fight()
