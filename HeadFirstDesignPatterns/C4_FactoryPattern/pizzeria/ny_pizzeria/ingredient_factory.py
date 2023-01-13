from ..ingredient_factory import PizzaIngredientFactory
from ..ingredients import ThinCrustDough, MarinaraSauce, ReggianoCheese, Garlic, Onion, Mushroom, RedPepper, \
    SlicedPepperoni, FreshClams


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
