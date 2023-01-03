from abc import ABC, abstractmethod
from enum import Enum


class Size(Enum):
    TALL = 0
    GRANDE = 1
    VENTI = 2


class Beverage(ABC):
    size = Size.TALL
    description = 'Unknown Beverage'

    def get_description(self):
        return self.description

    def get_size(self):
        return self.size

    def set_size(self, size):
        self.size = size

    @abstractmethod
    def cost(self):
        ...


class CondimentDecorator(Beverage):
    @abstractmethod
    def get_description(self):
        ...

    def get_size(self):
        ...


class Espresso(Beverage):
    def __init__(self):
        self.description = f'{self.size.name} Espresso'

    def cost(self):
        return 1.99


class HouseBlend(Beverage):
    def __init__(self):
        self.description = f'{self.size.name} House Blend Coffee'

    def cost(self):
        return .89


class DarkRoast(Beverage):
    def __init__(self):
        self.description = f'{self.size.name} Dark Roast Coffee'

    def cost(self):
        return .99


class Decaf(Beverage):
    def __init__(self):
        self.description = f'{self.size.name} Decaf'

    def cost(self):
        return 1.05


class Mocha(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ', Mocha'

    def cost(self):
        return self.beverage.cost() + .2


class Soy(CondimentDecorator):
    size_costs = {
        Size.TALL: .1,
        Size.GRANDE: .15,
        Size.VENTI: .2
    }

    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ', Soy'

    def cost(self):
        return self.beverage.cost() + self.size_costs[self.beverage.get_size()]


class Whip(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ', Whip'

    def cost(self):
        return self.beverage.cost() + .1


class SteamedMilk(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ', Steamed Milk'

    def cost(self):
        return self.beverage.cost() + .1


if __name__ == '__main__':
    beverage = Espresso()
    print(f'{beverage.get_description()} ${beverage.cost()}')

    beverage2 = DarkRoast()
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2 = Whip(beverage2)
    print(f'{beverage2.get_description()} ${beverage2.cost()}')

    beverage3 = HouseBlend()
    beverage3.set_size(Size.GRANDE)
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    print(f'{beverage3.get_description()} ${beverage3.cost()}')
