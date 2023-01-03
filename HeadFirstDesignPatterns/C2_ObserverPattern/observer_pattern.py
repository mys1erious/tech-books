from abc import ABC, abstractmethod


class Subject(ABC):
    __observers = []

    def register_observer(self, o):
        self.__observers.append(o)

    def remove_observer(self, o):
        self.__observers.remove(o)

    def notify_observers(self):
        for observer in self.__observers:
            observer.update(self)


class Observer(ABC):
    @abstractmethod
    def update(self, obs, *args):
        ...


class DisplayElement(ABC):
    def display(self):
        ...
