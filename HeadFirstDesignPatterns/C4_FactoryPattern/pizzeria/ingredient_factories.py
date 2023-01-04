from abc import ABC, abstractmethod

from HeadFirstDesignPatterns.C4_FactoryPattern.pizzeria.ingredients import ThinCrustDough, MarinaraSauce, \
    ReggianoCheese, FreshClams, ThickCrustDough, PlumTomatoSauce, MozzarellaCheese, FrozenClams, Garlic, Onion, \
    Mushroom, RedPepper, SlicedPepperoni, BlackOlives, Spinach, EggPlant, BBQSauce, ArtichokeHearts, MashedPotatoes, \
    Peanuts


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


class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        return ThinCrustDough()

    def create_sauce(self):
        return MarinaraSauce()

    def create_cheese(self):
        return ReggianoCheese()

    def create_veggies(self):
        return [Garlic(), Onion(), Mushroom(), RedPepper()]

    def create_pepperoni(self):
        return SlicedPepperoni()

    def create_clam(self):
        return FreshClams()


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        return ThickCrustDough()

    def create_sauce(self):
        return PlumTomatoSauce()

    def create_cheese(self):
        return MozzarellaCheese()

    def create_veggies(self):
        return [BlackOlives(), Spinach(), EggPlant()]

    def create_pepperoni(self):
        return SlicedPepperoni()

    def create_clam(self):
        return FrozenClams()


class CaliforniaPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        return ThickCrustDough()

    def create_sauce(self):
        return BBQSauce()

    def create_cheese(self):
        return MozzarellaCheese()

    def create_veggies(self):
        return [ArtichokeHearts(), MashedPotatoes(), Peanuts()]

    def create_pepperoni(self):
        return SlicedPepperoni()

    def create_clam(self):
        return FrozenClams()
