from abc import ABC, abstractmethod


# Abstract Factory Pattern
class PizzaIngredientFactory(ABC):
    @abstractmethod
    def create_dough(self):
        ...

    @abstractmethod
    def create_sauce(self):
        ...

    @abstractmethod
    def create_cheese(self):
        ...

    @abstractmethod
    def create_veggies(self):
        ...

    @abstractmethod
    def create_pepperoni(self):
        ...

    @abstractmethod
    def create_clam(self):
        ...
