from abc import ABC, abstractmethod
import random as rnd


class State(ABC):
    @abstractmethod
    def insert_quarter(self):
        ...

    @abstractmethod
    def eject_quarter(self):
        ...

    @abstractmethod
    def turn_crank(self):
        ...

    @abstractmethod
    def dispense(self):
        ...


class NoQuarterState(State):
    def __init__(self, gumball_machine):
        self.__gumball_machine = gumball_machine

    def insert_quarter(self):
        print('You inserted a quarter')
        self.__gumball_machine.set_state(self.__gumball_machine.has_quarter_state)

    def eject_quarter(self):
        print('You havent inserted a quarter')

    def turn_crank(self):
        print('You turned but there is no quarter')

    def dispense(self):
        print('You need to pay first')


class HasQuarterState(State):
    def __init__(self, gumball_machine):
        self.__gumball_machine = gumball_machine

    def insert_quarter(self):
        print('You cant insert another quarter')

    def eject_quarter(self):
        print('Quarter returned')
        self.__gumball_machine.set_state(self.__gumball_machine.no_quarter_state)

    def turn_crank(self):
        print('You turned...')
        # winner = rnd.randint(0, 10) == 0
        winner = True
        if winner and self.__gumball_machine.count > 1:
            self.__gumball_machine.set_state(self.__gumball_machine.winner_state)
        else:
            self.__gumball_machine.set_state(self.__gumball_machine.sold_state)

    def dispense(self):
        print('No gumball dispensed')


class SoldState(State):
    def __init__(self, gumball_machine):
        self.__gumball_machine = gumball_machine

    def insert_quarter(self):
        print('Please wait, we are already giving you a gumball')

    def eject_quarter(self):
        print('Sorry, you already turned the crank')

    def turn_crank(self):
        print('Turning twice doesnt get you another gumball')

    def dispense(self):
        self.__gumball_machine.release_ball()
        if self.__gumball_machine.count > 0:
            self.__gumball_machine.state = self.__gumball_machine.no_quarter_state
        else:
            print('Oops, out of gumballs')
            self.__gumball_machine.state = self.__gumball_machine.sold_out_state


class SoldOutState(State):
    def __init__(self, gumball_machine):
        self.__gumball_machine = gumball_machine

    def insert_quarter(self):
        print('You cant insert a quarter, the machine is sold out')

    def eject_quarter(self):
        print('U cant eject, you havent inserted a quarter yet')

    def turn_crank(self):
        print('You turned but there are no gumballs')

    def dispense(self):
        print('No gumball dispensed')


class WinnerState(State):
    def __init__(self, gumball_machine):
        self.__gumball_machine = gumball_machine

    def insert_quarter(self):
        print('You cant insert a quarter, the machine is sold out')

    def eject_quarter(self):
        print('U cant eject, you havent inserted a quarter yet')

    def turn_crank(self):
        print('You turned but there are no gumballs')

    def dispense(self):
        self.__gumball_machine.release_ball()
        if self.__gumball_machine.count == 0:
            self.__gumball_machine.set_state(self.__gumball_machine.sold_out_state)
        else:
            self.__gumball_machine.release_ball()
            print('YOU ARE A WINNER! You got two gumballs for your quarter')
            if self.__gumball_machine.count > 0:
                self.__gumball_machine.set_state(self.__gumball_machine.no_quarter_state)
            else:
                print('Oops, out of gumballs')
                self.__gumball_machine.set_state(self.__gumball_machine.sold_out_state)


class GumballMachine:
    def __init__(self, number_gumballs):
        self.__sold_out_state = SoldOutState(self)
        self.__no_quarter_state = NoQuarterState(self)
        self.__has_quarter_state = HasQuarterState(self)
        self.__sold_state = SoldState(self)
        self.__winner_state = WinnerState(self)

        self.refill(number_gumballs)

    @property
    def sold_out_state(self):
        return self.__sold_out_state

    @property
    def no_quarter_state(self):
        return self.__no_quarter_state

    @property
    def has_quarter_state(self):
        return self.__has_quarter_state

    @property
    def sold_state(self):
        return self.__sold_state

    @property
    def winner_state(self):
        return self.__winner_state

    @property
    def count(self):
        return self.__count

    def insert_quarter(self):
        self.__state.insert_quarter()

    def eject_quarter(self):
        self.__state.eject_quarter()

    def turn_crank(self):
        self.__state.turn_crank()
        self.__state.dispense()

    def set_state(self, state):
        self.__state = state

    def release_ball(self):
        print('A gumball comes rolling out the slot...')
        if self.__count != 0:
            self.__count -= 1

    def refill(self, number_gumballs):
        self.__count = number_gumballs
        if number_gumballs > 0:
            self.__state = self.__no_quarter_state
        else:
            self.__state = self.__sold_out_state

    def __str__(self):
        return f'machine state --> {type(self.__state).__name__}'


if __name__ == '__main__':
    gumball_machine = GumballMachine(5)
    print(gumball_machine)

    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()

    print(gumball_machine)

    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()
    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()

    print(gumball_machine)
