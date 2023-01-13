from ..store_factory import PizzaStore
from ..pizzas import CheesePizza, ClamPizza
from .ingredient_factory import CaliforniaPizzaIngredientFactory


class CaliforniaPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        pizza = None
        ingredient_factory = CaliforniaPizzaIngredientFactory()

        if pizza_type == 'cheese':
            pizza = CheesePizza(ingredient_factory)
            pizza.name = 'California Style Cheese Pizza'
        elif pizza_type == 'clam':
            pizza = ClamPizza(ingredient_factory)
            pizza.name = 'California Style Clam Pizza'
        # elif pizza_type == 'pepperoni':
        #     pizza = PepperoniPizza(ingredient_factory)
        #     pizza.name = 'California Style Pepperoni Pizza'
        # elif pizza_type == 'veggie':
        #     pizza = VeggiePizza(ingredient_factory)
        #     pizza.name = 'California Style Vegie Pizza'

        return pizza
