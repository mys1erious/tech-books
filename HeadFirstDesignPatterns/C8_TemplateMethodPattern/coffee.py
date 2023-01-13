from abc import ABC, abstractmethod


class CaffeineBeverage(ABC):
    # Template Method
    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.customer_wants_condiments():
            self.add_condiments()

    # Primitive methods
    @abstractmethod
    def brew(self):
        ...

    @abstractmethod
    def add_condiments(self):
        ...

    # Concrete methods
    def boil_water(self):
        print('Boiling water')

    def pour_in_cup(self):
        print('Pouring in cup')

    # Hook
    def customer_wants_condiments(self):
        return True


class Coffee(CaffeineBeverage):
    def brew(self):
        print('Dripping Coffee through filter')

    def add_condiments(self):
        print('Adding Sugar and Milk')

    def customer_wants_condiments(self):
        ans = input('Would you like milk and sugar with your coffee (y/n)? ')
        if ans.lower().startswith('y'):
            return True
        return False


class Tea(CaffeineBeverage):
    def brew(self):
        print('Steeping the tea')

    def add_condiments(self):
        print('Adding Lemon')


if __name__ == '__main__':
    tea = Tea()
    coffee = Coffee()

    print('Making Tea...')
    tea.prepare_recipe()

    print('Making Coffee...')
    coffee.prepare_recipe()
