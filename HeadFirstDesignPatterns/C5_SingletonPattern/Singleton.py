# Doesnt work in python cuz cant make private constructor
# class Singleton:
#     __unique_instance = None
#
#     @staticmethod
#     def get_instance():
#         if Singleton.__unique_instance is None:
#             Singleton.__unique_instance = Singleton()
#         return Singleton.__unique_instance


# Python implementation of Singleton?
class SingletonBase(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(SingletonBase, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]


class Singleton(metaclass=SingletonBase):
    def hello(self):
        print('hello from ' + str(self))


if __name__ == '__main__':
    s = Singleton()
    s.hello()
    s1 = Singleton()
    s1.hello()
