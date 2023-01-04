from abc import ABC, abstractmethod


class Dough(ABC):
    @abstractmethod
    def __str__(self):
        ...


class ThickCrustDough(Dough):
    def __str__(self):
        return 'ThickCrustDough'


class ThinCrustDough(Dough):
    def __str__(self):
        return 'ThinCrustDough'


class Sauce(ABC):
    @abstractmethod
    def __str__(self):
        ...


class PlumTomatoSauce(Sauce):
    def __str__(self):
        return 'PlumTomatoSauce'


class MarinaraSauce(Sauce):
    def __str__(self):
        return 'MarinaraSauce'


class BBQSauce(Sauce):
    def __str__(self):
        return 'BBQSauce'


class Cheese(ABC):
    @abstractmethod
    def __str__(self):
        ...


class MozzarellaCheese(Cheese):
    def __str__(self):
        return 'MozzarellaCheese'


class ReggianoCheese(Cheese):
    def __str__(self):
        return 'ReggianoCheese'


class Clams(ABC):
    @abstractmethod
    def __str__(self):
        ...


class FrozenClams(Clams):
    def __str__(self):
        return 'FrozenClams'


class FreshClams(Clams):
    def __str__(self):
        return 'FreshClams'


class Vegetable(ABC):
    @abstractmethod
    def __str__(self):
        ...


class Garlic(Vegetable):
    def __str__(self):
        return 'Garlic'


class Onion(Vegetable):
    def __str__(self):
        return 'Onion'


class Mushroom(Vegetable):
    def __str__(self):
        return 'Mushroom'


class RedPepper(Vegetable):
    def __str__(self):
        return 'RedPepper'


class BlackOlives(Vegetable):
    def __str__(self):
        return 'BlackOlives'


class Spinach(Vegetable):
    def __str__(self):
        return 'Spinach'


class EggPlant(Vegetable):
    def __str__(self):
        return 'EggPlant'


class ArtichokeHearts(Vegetable):
    def __str__(self):
        return 'ArtichokeHearts'


class MashedPotatoes(Vegetable):
    def __str__(self):
        return 'MashedPotatoes'


class Peanuts(Vegetable):
    def __str__(self):
        return 'Peanuts'


class Pepperoni(ABC):
    @abstractmethod
    def __str__(self):
        ...


class SlicedPepperoni(Pepperoni):
    def __str__(self):
        return 'SlicedPepperoni'
