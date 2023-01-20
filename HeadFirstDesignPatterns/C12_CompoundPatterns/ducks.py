"""
Set of patterns working together,
not a Compound pattern,
Design is forced and artificial
"""

from abc import ABC, abstractmethod


class QuackObservable(ABC):
    @abstractmethod
    def register_observer(self, observer):
        ...

    @abstractmethod
    def notify_observers(self):
        ...


class Observable(QuackObservable):
    def __init__(self, duck):
        self.__observers = []
        self.__duck = duck

    def register_observer(self, observer):
        self.__observers.append(observer)

    def notify_observers(self):
        iterator = self.__observers.__iter__()
        observer = next(iterator, None)
        while observer:
            observer.update(self.__duck)
            observer = next(iterator, None)


class Observer(ABC):
    @abstractmethod
    def update(self, duck):
        ...


class Quackologist(Observer):
    def update(self, duck):
        print(f'Quackologist: {duck} just quacked.')


class Quackable(QuackObservable):
    @abstractmethod
    def quack(self):
        ...

    def __str__(self):
        return f'{type(self).__name__}'


class Flock(Quackable):
    def __init__(self):
        self.__quackers = []

    def add(self, quacker):
        self.__quackers.append(quacker)

    def quack(self):
        iterator = self.__quackers.__iter__()
        quacker = next(iterator, None)
        while quacker:
            quacker.quack()
            quacker = next(iterator, None)

    def register_observer(self, observer):
        for quacker in self.__quackers:
            quacker.register_observer(observer)

    def notify_observers(self):
        ...


class MallardDuck(Quackable):
    def __init__(self):
        self.__observable = Observable(self)

    def quack(self):
        print('Quack')
        self.notify_observers()

    def register_observer(self, observer):
        self.__observable.register_observer(observer)

    def notify_observers(self):
        self.__observable.notify_observers()


class RedheadDuck(Quackable):
    def __init__(self):
        self.__observable = Observable(self)

    def quack(self):
        print('Quack')
        self.notify_observers()

    def register_observer(self, observer):
        self.__observable.register_observer(observer)

    def notify_observers(self):
        self.__observable.notify_observers()


class DuckCall(Quackable):
    def __init__(self):
        self.__observable = Observable(self)

    def quack(self):
        print('Kwak')
        self.notify_observers()

    def register_observer(self, observer):
        self.__observable.register_observer(observer)

    def notify_observers(self):
        self.__observable.notify_observers()


class RubberDuck(Quackable):
    def __init__(self):
        self.__observable = Observable(self)

    def quack(self):
        print('Squeak')
        self.notify_observers()

    def register_observer(self, observer):
        self.__observable.register_observer(observer)

    def notify_observers(self):
        self.__observable.notify_observers()


class Goose:
    def honk(self):
        print('Honk')


class GooseAdapter(Quackable):
    def __init__(self, goose):
        self.__observable = Observable(self)
        self.__goose = goose

    def quack(self):
        self.__goose.honk()
        self.notify_observers()

    def register_observer(self, observer):
        self.__observable.register_observer(observer)

    def notify_observers(self):
        self.__observable.notify_observers()


class QuackCounter(Quackable):
    __number_of_quacks = 0

    def __init__(self, duck):
        self.__observable = Observable(self)
        self.__duck = duck

    def quack(self):
        self.__duck.quack()
        QuackCounter.__number_of_quacks += 1
        self.notify_observers()

    @staticmethod
    def get_quacks():
        return QuackCounter.__number_of_quacks

    def register_observer(self, observer):
        self.__observable.register_observer(observer)

    def notify_observers(self):
        self.__observable.notify_observers()

    def __str__(self):
        return str(self.__duck)


class AbstractDuckFactory(ABC):
    @abstractmethod
    def create_mallard_duck(self):
        ...

    @abstractmethod
    def create_redhead_duck(self):
        ...

    @abstractmethod
    def create_duck_call(self):
        ...

    @abstractmethod
    def create_rubber_duck(self):
        ...


class DuckFactory(AbstractDuckFactory):
    def create_mallard_duck(self):
        return MallardDuck()

    def create_redhead_duck(self):
        return RedheadDuck()

    def create_duck_call(self):
        return DuckCall()

    def create_rubber_duck(self):
        return RubberDuck()


class CountingDuckFactory(AbstractDuckFactory):
    def create_mallard_duck(self):
        return QuackCounter(MallardDuck())

    def create_redhead_duck(self):
        return QuackCounter(RedheadDuck())

    def create_duck_call(self):
        return QuackCounter(DuckCall())

    def create_rubber_duck(self):
        return QuackCounter(RubberDuck())


def simulate():
    duck_factory = CountingDuckFactory()

    print('\nDuck Simulator:')
    perf_quack = lambda duck: duck.quack()

    redhead_duck = duck_factory.create_redhead_duck()
    duck_call = duck_factory.create_duck_call()
    rubber_duck = duck_factory.create_rubber_duck()
    goose_duck = GooseAdapter(Goose())

    flock_of_ducks = Flock()
    flock_of_ducks.add(redhead_duck)
    flock_of_ducks.add(duck_call)
    flock_of_ducks.add(rubber_duck)
    flock_of_ducks.add(goose_duck)

    mallard_one = duck_factory.create_mallard_duck()
    mallard_two = duck_factory.create_mallard_duck()
    mallard_three = duck_factory.create_mallard_duck()
    mallard_four = duck_factory.create_mallard_duck()

    flock_of_mallards = Flock()
    flock_of_mallards.add(mallard_one)
    flock_of_mallards.add(mallard_two)
    flock_of_mallards.add(mallard_three)
    flock_of_mallards.add(mallard_four)

    flock_of_ducks.add(flock_of_mallards)

    quackologist = Quackologist()
    flock_of_ducks.register_observer(quackologist)
    perf_quack(flock_of_ducks)

    print(f'The ducks quacked {QuackCounter.get_quacks()} times')


if __name__ == '__main__':
    simulate()
