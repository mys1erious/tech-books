from abc import ABC, abstractmethod


class MenuItem:
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


class Menu(ABC):
    @abstractmethod
    def create_iterator(self):
        ...


class PancakeHouseMenu(Menu):
    def __init__(self):
        self.__menu_items = []

        self.add_item(
            'K&B Pancake Breakfast',
            'Pancake with scrambled eggs, and toast',
            True,
            2.00
        )
        self.add_item(
            'Regular Pancake Breakfast',
            'Pancakes with fried eggs, sausage',
            False,
            2.99
        )
        self.add_item(
            'Blueberry Pancakes',
            'Pancakes made with fresh blueberries',
            True,
            3.59
        )
        self.add_item(
            'Waffles',
            'Waffles, with your choice of blueberries or strawberries',
            True,
            3.59
        )

    def add_item(self, name, description, vegetarian, price):
        self.__menu_items.append(MenuItem(name, description, vegetarian, price))

    def create_iterator(self):
        return self.__menu_items.__iter__()
        # return PancakeHouseMenuIterator(self.__menu_items)


class DinerMenu(Menu):
    MAX_ITEMS = 6

    def __init__(self):
        self.__number_of_items = 0
        # Array imitation
        self.__menu_items = [0] * self.MAX_ITEMS

        self.add_item(
            'Vegetarian BLT',
            'Bacon with lettuce & tomato on whole wheat',
            True,
            2.99
        )
        self.add_item(
            'BLT',
            'Bacon with lettuce & tomato on whole wheat',
            False,
            2.99
        )
        self.add_item(
            'Soup of the day',
            'Soup of the day, with a side of potato salad',
            False,
            3.29
        )
        self.add_item(
            'Hotdog',
            'A hot dog with saurkraut, relish, onions, topped with cheese',
            False,
            3.05
        )
        self.add_item(
            'Hotdog2',
            'A hot dog2 with saurkraut, relish, onions, topped with cheese',
            False,
            3.15
        )
        self.add_item(
            'Hotdog3',
            'A hot dog3 with saurkraut, relish, onions, topped with cheese',
            False,
            3.45
        )

    def add_item(self, name, description, vegetarian, price):
        menu_item = MenuItem(name, description, vegetarian, price)
        if self.__number_of_items >= self.MAX_ITEMS:
            print('Sorry, menu is full! Can\'t add item to menu')
        else:
            self.__menu_items[self.__number_of_items] = menu_item
            self.__number_of_items += 1

    def create_iterator(self):
        return self.__menu_items.__iter__()
        # return DinerMenuIterator(self.__menu_items)


class CafeMenu(Menu):
    def __init__(self):
        self.__menu_items = {}
        self.add_item(
            'Veggie Burger and Air Fries',
            'Veggie burger on a whole wheat bun, lettuce, tomato, and fries',
            True,
            3.99
        )
        self.add_item(
            'Soup of the day',
            'A cup of the soup of the day, with a side salad',
            False,
            3.69
        )
        self.add_item(
            'Burrito',
            'A large burrito, with whole pinto beans, salsa, guacamole',
            True,
            4.29
        )

    def add_item(self, name, description, vegetarian, price):
        menu_item = MenuItem(name, description, vegetarian, price)
        self.__menu_items[menu_item.name] = menu_item

    def create_iterator(self):
        return self.__menu_items.values().__iter__()


# Can use builtin __iter__() or use custom-created Iterator
class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        ...

    @abstractmethod
    def __next__(self):
        ...

    @abstractmethod
    def remove(self):
        ...


class PancakeHouseMenuIterator(Iterator):
    def __init__(self, items):
        self.__items = items
        self.__position = 0

    def __next__(self):
        menu_item = self.__items[self.__position]
        self.__position += 1
        return menu_item

    def has_next(self):
        if self.__position >= len(self.__items) or self.__items[self.__position] is None:
            return False
        return True

    def remove(self):
        self.__items.pop()


class DinerMenuIterator(Iterator):
    def __init__(self, items):
        self.__items = items
        self.__position = 0

    def __next__(self):
        menu_item = self.__items[self.__position]
        self.__position += 1
        return menu_item

    def has_next(self):
        if self.__position >= len(self.__items) or self.__items[self.__position] is None:
            return False
        return True

    def remove(self):
        self.__items.pop()


class Waitress:
    def __init__(self, menus):
        self.menus = menus

    def print_menu(self):
        menu_iterator = self.menus.__iter__()
        menu = next(menu_iterator, None)
        while menu is not None:
            self.__print_menu(menu.create_iterator())
            menu = next(menu_iterator, None)

    def __print_menu(self, iterator):
        menu_item = next(iterator, None)
        while menu_item is not None:
            print(f'{menu_item.name}, ', end='')
            print(f'{menu_item.price} -- ', end='')
            print(menu_item.description)

            menu_item = next(iterator, None)


if __name__ == '__main__':
    pancake_house_menu = PancakeHouseMenu()
    diner_menu = DinerMenu()
    cafe_menu = CafeMenu()

    waitress = Waitress([pancake_house_menu, diner_menu, cafe_menu])
    waitress.print_menu()
