from ..ingredient_factory import PizzaIngredientFactory
from ..ingredients import ThickCrustDough, BBQSauce, MozzarellaCheese, ArtichokeHearts, MashedPotatoes, Peanuts, \
    SlicedPepperoni, FrozenClams


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
