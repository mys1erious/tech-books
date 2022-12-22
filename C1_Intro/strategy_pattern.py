from abc import ABC, abstractmethod


class Duck(ABC):
    fly_behaviour = None
    quack_behaviour = None

    def perform_fly(self):
        self.fly_behaviour.fly()

    def perform_quack(self):
        self.quack_behaviour.quack()

    def swim(self):
        print('Duck is swimming')

    @abstractmethod
    def display(self):
        ...

    def set_fly_behaviour(self, fb):
        self.fly_behaviour = fb

    def set_quack_behaviour(self, qb):
        self.quack_behaviour = qb


class MallardDuck(Duck):
    def __init__(self):
        self.quack_behaviour = Quack()
        self.fly_behaviour = FlyWithWings()

    def display(self):
        print('I am a real Mallard duck!')


class ModelDuck(Duck):
    def __init__(self):
        self.fly_behaviour = FlyNoWay()
        self.quack_behaviour = Quack()

    def display(self):
        print('I am a model duck')


class FlyBehaviour(ABC):
    @abstractmethod
    def fly(self):
        pass


class FlyWithWings(FlyBehaviour):
    def fly(self):
        print('FlyWithWings behaviour')


class FlyNoWay(FlyBehaviour):
    def fly(self):
        print('FlyNoWay behaviour')


class FlyRocketPowered(FlyBehaviour):
    def fly(self):
        print('I am flying with a rocket')


class QuackBehaviour(ABC):
    @abstractmethod
    def quack(self):
        pass


class Quack(QuackBehaviour):
    def quack(self):
        print('Quack behaviour')


class Squeak(QuackBehaviour):
    def quack(self):
        print('Squeak behaviour')


class MuteQuack(QuackBehaviour):
    def quack(self):
        print('MuteQuack behaviour')


if __name__ == '__main__':
    mallard_duck = MallardDuck()
    mallard_duck.perform_fly()
    mallard_duck.perform_quack()

    model = ModelDuck()
    model.perform_fly()
    model.set_fly_behaviour(FlyRocketPowered())
    model.perform_fly()
