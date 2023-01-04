from abc import ABC, abstractmethod


class PizzaStore:
    def __init__(self, factory):
        self.factory = factory

    def order_pizza(self, pizza_type):
        pizza = self.factory.create_pizza(pizza_type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza


class Pizza(ABC):
    def prepare(self):
        ...

    def bake(self):
        ...

    def cut(self):
        ...

    def box(self):
        ...


class CheesePizza(Pizza):
    ...


class PepperoniPizza(Pizza):
    ...


class ClamPizza(Pizza):
    ...


class VeggiePizza(Pizza):
    ...


class SimplePizzaFactory:
    def create_pizza(self, pizza_type):
        pizza = None

        if pizza_type == 'cheese':
            pizza = CheesePizza()
        elif pizza_type == 'pepperoni':
            pizza = PepperoniPizza()
        elif pizza_type == 'clam':
            pizza = ClamPizza()
        elif pizza_type == 'veggie':
            pizza = VeggiePizza()

        return pizza
