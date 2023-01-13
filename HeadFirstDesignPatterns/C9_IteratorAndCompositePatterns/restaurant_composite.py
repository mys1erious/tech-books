from abc import ABC, abstractmethod


# class PancakeHouseMenu(Menu):
#     def __init__(self):
#         self.__menu_items = []
#
#         self.add_item(
#             'K&B Pancake Breakfast',
#             'Pancake with scrambled eggs, and toast',
#             True,
#             2.00
#         )
#         self.add_item(
#             'Regular Pancake Breakfast',
#             'Pancakes with fried eggs, sausage',
#             False,
#             2.99
#         )
#         self.add_item(
#             'Blueberry Pancakes',
#             'Pancakes made with fresh blueberries',
#             True,
#             3.59
#         )
#         self.add_item(
#             'Waffles',
#             'Waffles, with your choice of blueberries or strawberries',
#             True,
#             3.59
#         )
#
#     def add_item(self, name, description, vegetarian, price):
#         self.__menu_items.append(MenuItem(name, description, vegetarian, price))
#
#     def create_iterator(self):
#         return self.__menu_items.__iter__()
#
#
# class DinerMenu(Menu):
#     MAX_ITEMS = 6
#
#     def __init__(self):
#         self.__number_of_items = 0
#         # Array imitation
#         self.__menu_items = [0] * self.MAX_ITEMS
#
#         self.add_item(
#             'Vegetarian BLT',
#             'Bacon with lettuce & tomato on whole wheat',
#             True,
#             2.99
#         )
#         self.add_item(
#             'BLT',
#             'Bacon with lettuce & tomato on whole wheat',
#             False,
#             2.99
#         )
#         self.add_item(
#             'Soup of the day',
#             'Soup of the day, with a side of potato salad',
#             False,
#             3.29
#         )
#         self.add_item(
#             'Hotdog',
#             'A hot dog with saurkraut, relish, onions, topped with cheese',
#             False,
#             3.05
#         )
#         self.add_item(
#             'Hotdog2',
#             'A hot dog2 with saurkraut, relish, onions, topped with cheese',
#             False,
#             3.15
#         )
#         self.add_item(
#             'Hotdog3',
#             'A hot dog3 with saurkraut, relish, onions, topped with cheese',
#             False,
#             3.45
#         )
#
#     def add_item(self, name, description, vegetarian, price):
#         menu_item = MenuItem(name, description, vegetarian, price)
#         if self.__number_of_items >= self.MAX_ITEMS:
#             print('Sorry, menu is full! Can\'t add item to menu')
#         else:
#             self.__menu_items[self.__number_of_items] = menu_item
#             self.__number_of_items += 1
#
#     def create_iterator(self):
#         return self.__menu_items.__iter__()
#
#
# class CafeMenu(Menu):
#     def __init__(self):
#         self.__menu_items = {}
#         self.add_item(
#             'Veggie Burger and Air Fries',
#             'Veggie burger on a whole wheat bun, lettuce, tomato, and fries',
#             True,
#             3.99
#         )
#         self.add_item(
#             'Soup of the day',
#             'A cup of the soup of the day, with a side salad',
#             False,
#             3.69
#         )
#         self.add_item(
#             'Burrito',
#             'A large burrito, with whole pinto beans, salsa, guacamole',
#             True,
#             4.29
#         )
#
#     def add_item(self, name, description, vegetarian, price):
#         menu_item = MenuItem(name, description, vegetarian, price)
#         self.__menu_items[menu_item.name] = menu_item
#
#     def create_iterator(self):
#         return self.__menu_items.values().__iter__()


# !!! Need to fix this iterator !!!
class CompositeIterator:
    def __init__(self, iterator):
        self.__stack = []
        self.__stack.append(iterator)

    def __next__(self):
        if self.has_next():
            iterator = self.__stack[-1]
            component = iterator.__next__()
            self.__stack.append(component.create_iterator())
            return component
        else:
            return None

    def has_next(self):
        if len(self.__stack) == 0:
            return False

        iterator = self.__stack[-1]
        iterator_next = next(iterator, None)
        if iterator_next is None:
            self.__stack.pop()
            return self.has_next()
        else:
            return True


class MenuComponent(ABC):
    def add(self, menu_component):
        raise AttributeError()

    def remove(self, menu_component):
        raise AttributeError()

    def get_child(self, i):
        raise AttributeError()

    def name(self):
        raise AttributeError()

    def description(self):
        raise AttributeError()

    def price(self):
        raise AttributeError()

    def vegetarian(self):
        raise AttributeError()

    def print(self):
        raise AttributeError()

    def create_iterator(self):
        raise AttributeError()


class MenuItem(MenuComponent):
    def __init__(self, name, description, vegetarian, price):
        self.__name = name
        self.__description = description
        self.__vegetarian = vegetarian
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    @property
    def vegetarian(self):
        return self.__vegetarian

    @property
    def price(self):
        return self.__price

    def print(self):
        print(f'  {self.name}', end='')
        if self.vegetarian:
            print('(v)', end='')
        print(f', {self.price}')
        print(f'    -- {self.description}')

    def create_iterator(self):
        return iter([])


class Menu(MenuComponent):
    def __init__(self, name, description):
        self.__menu_components = []
        self.__name = name
        self.__description = description

        self.__iterator = None

    def add(self, menu_component):
        self.__menu_components.append(menu_component)

    def remove(self, menu_component):
        self.__menu_components.remove(menu_component)

    def get_child(self, i):
        return self.__menu_components[i]

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    def print(self):
        print(f'\n{self.name}', end='')
        print(f', {self.description}')
        print('-'*50)

        iterator = self.__menu_components.__iter__()
        menu_component = next(iterator, None)
        while menu_component is not None:
            menu_component.print()
            menu_component = next(iterator, None)

    def create_iterator(self):
        if self.__iterator is None:
            self.__iterator = CompositeIterator(self.__menu_components.__iter__())
        return self.__iterator


class Waitress:
    def __init__(self, menus):
        self.__menus = menus

    def print_menu(self):
        self.__menus.print()

    def print_vegetarian_menu(self):
        iterator = self.__menus.create_iterator()

        print(f'\nVEGETARIAN MENU\n----')
        menu_component = next(iterator, None)
        while menu_component is not None:
            try:
                if menu_component.vegetarian:
                    menu_component.print()
            except AttributeError:
                ...
            menu_component = next(iterator, None)


if __name__ == '__main__':
    # pancake_house_menu = PancakeHouseMenu()
    # diner_menu = DinerMenu()
    # cafe_menu = CafeMenu()
    pancake_house_menu = Menu('PANCAKE HOUSE MENU', 'Breakfast')
    diner_menu = Menu('DINER MENU', 'Lunch')
    cafe_menu = Menu('CAFE MENU', 'Dinner')
    dessert_menu = Menu('DESSERT MENU', 'Dessert of course')

    menus = Menu('ALL MENUS', 'All menus combined')
    menus.add(pancake_house_menu)
    menus.add(diner_menu)
    menus.add(cafe_menu)

    diner_menu.add(MenuItem(
        'Pasta',
        'Spaghetti with Marinara Sauce, and a slice of sourdough bread',
        False,
        3.89
    ))
    diner_menu.add(dessert_menu)

    dessert_menu.add(MenuItem(
        'Apple Pie',
        'Apple Pie with a flakey crust, topped with vanilla icecream',
        True,
        1.59
    ))

    waitress = Waitress(menus)
    # waitress.print_menu()
    waitress.print_vegetarian_menu()
