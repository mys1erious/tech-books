from ..store_factory import PizzaStore
from ..pizzas import CheesePizza, ClamPizza
from .ingredient_factory import NYPizzaIngredientFactory


class NYPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        pizza = None
        ingredient_factory = NYPizzaIngredientFactory()

        if pizza_type == 'cheese':
            pizza = CheesePizza(ingredient_factory)
            pizza.name = 'NY Style Sauce and Cheese Pizza'
        elif pizza_type == 'clam':
            pizza = ClamPizza(ingredient_factory)
            pizza.name = 'NY Style Clam Pizza'
        # elif pizza_type == 'pepperoni':
        #     pizza = PepperoniPizza(ingredient_factory)
        #     pizza.name = 'NY Style Pepperoni Pizza'
        # elif pizza_type == 'veggie':
        #     pizza = VeggiePizza(ingredient_factory)
        #     pizza.name = 'NY Style Vegie Pizza'

        return pizza
