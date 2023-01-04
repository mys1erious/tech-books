from abc import ABC, abstractmethod


class Pizza(ABC):
    def __init__(self):
        self.name = None
        self.dough = None
        self.sauce = None
        self.veggies = []
        self.cheese = None
        self.pepperoni = None
        self.clam = None

    @abstractmethod
    def prepare(self):
        ...

    def bake(self):
        print('Bake for 25 min at 350')

    def cut(self):
        print('Cutting the pizza into diagonal slices')

    def box(self):
        print('Place pizza in official PizzaStore box')

    def get_name(self):
        return self.name


class CheesePizza(Pizza):
    def __init__(self, ingredient_factory):
        super().__init__()
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print(f'Preparing {self.name}')
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()


class ClamPizza(Pizza):
    def __init__(self, ingredient_factory):
        super().__init__()
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print(f'Preparing {self.name}')
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.clam = self.ingredient_factory.create_clam()
