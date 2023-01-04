from abc import ABC, abstractmethod
from .pizzas import CheesePizza, ClamPizza
from .ingredient_factories import NYPizzaIngredientFactory, ChicagoPizzaIngredientFactory, \
    CaliforniaPizzaIngredientFactory


# Factory Method Pattern
class PizzaStore(ABC):
    def order_pizza(self, pizza_type):
        pizza = self.create_pizza(pizza_type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza

    @abstractmethod
    def create_pizza(self, pizza_type):
        ...


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
