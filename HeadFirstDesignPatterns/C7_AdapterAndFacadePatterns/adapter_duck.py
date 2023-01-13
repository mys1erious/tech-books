from abc import ABC


class Duck(ABC):
    def quack(self):
        ...

    def fly(self, distance):
        ...


class MallardDuck(Duck):
    def quack(self):
        print('Quack')

    def fly(self, distance=50):
        print(f'I`m flying for {distance}m distance')


class Turkey(ABC):
    def gobble(self):
        ...

    def fly(self):
        ...


class WildTurkey(Turkey):
    def gobble(self):
        print('Gobble gobble')

    def fly(self):
        print(f'I`m flying a 10m distance')


class TurkeyAdapter(Duck):
    def __init__(self, turkey):
        self.turkey = turkey

    def quack(self):
        self.turkey.gobble()

    def fly(self, distance=50):
        for _ in range(5):
            self.turkey.fly()


class DuckAdapter(Turkey):
    def __init__(self, duck):
        self.duck = duck

    def gobble(self):
        self.duck.quack()

    def fly(self):
        self.duck.fly(distance=10)


def test_duck(duck):
    duck.quack()
    duck.fly()


def test_turkey(turkey):
    turkey.gobble()
    turkey.fly()


if __name__ == '__main__':
    duck = MallardDuck()
    turkey = WildTurkey()
    turkey_adapter = TurkeyAdapter(turkey)
    duck_adapter = DuckAdapter(duck)

    print('The Turkey says...')
    test_turkey(turkey)

    print('The Duck says...')
    test_duck(duck)

    print('The TurkeyAdapter says...')
    test_duck(turkey_adapter)

    print('The DuckAdapter says...')
    test_turkey(duck_adapter)
