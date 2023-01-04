from HeadFirstDesignPatterns.C4_FactoryPattern.pizzeria.stores import NYPizzaStore, ChicagoPizzaStore


if __name__ == '__main__':
    ny_store = NYPizzaStore()
    chicago_store = ChicagoPizzaStore()

    pizza = ny_store.order_pizza('cheese')
    print(f'Ethan ordered a {pizza.get_name()}')
    print(pizza.dough)
    print(pizza.sauce)
    print(pizza.veggies)
    print(pizza.cheese)
    print(pizza.pepperoni)
    print(pizza.clam)
    print()

    pizza = chicago_store.order_pizza('clam')
    print(f'Joel ordered a {pizza.get_name()}')
    print(pizza.dough)
    print(pizza.sauce)
    print(pizza.veggies)
    print(pizza.cheese)
    print(pizza.pepperoni)
    print(pizza.clam)
