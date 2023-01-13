from ..store_factory import PizzaStore
from ..pizzas import CheesePizza, ClamPizza
from .ingredient_factory import ChicagoPizzaIngredientFactory


class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        pizza = None
        ingredient_factory = ChicagoPizzaIngredientFactory()

        if pizza_type == 'cheese':
            pizza = CheesePizza(ingredient_factory)
            pizza.name = 'Chicago Style Deep Cheese Pizza'
        elif pizza_type == 'clam':
            pizza = ClamPizza(ingredient_factory)
            pizza.name = 'Chicago Style Clam Pizza'
        # elif pizza_type == 'pepperoni':
        #     pizza = PepperoniPizza(ingredient_factory)
        #     pizza.name = 'Chicago Style Pepperoni Pizza'
        # elif pizza_type == 'veggie':
        #     pizza = VeggiePizza(ingredient_factory)
        #     pizza.name = 'Chicago Style Vegie Pizza'

        return pizza
