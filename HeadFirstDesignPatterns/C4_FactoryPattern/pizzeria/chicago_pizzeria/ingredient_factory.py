from ..ingredient_factory import PizzaIngredientFactory
from ..ingredients import ThickCrustDough, PlumTomatoSauce, MozzarellaCheese, BlackOlives, Spinach, EggPlant, \
    SlicedPepperoni, FrozenClams


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
