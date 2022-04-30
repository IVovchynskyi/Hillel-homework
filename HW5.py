"""
1) Реализовать класс который бы производил разные операции над 2мя переданными числами.

Пример Использования:

proccess_input = ProcessInput(a=20, b=10)
print(proccess_input.add()). # выведет 30
print(proccess_input.subtract()). # выведет 10
print(proccess_input.multiple()). # выведет 200
print(proccess_input.divide()). # выведет 2
"""

from typing import Union
class ProcessInput:
    """
    the class to perform some actions with two input digits
    """
    def __init__(self, a: Union[int, float], b: Union[int, float]):
       self.a = a
       self.b = b

    def add(self):
        try:
            return self.a + self.b
        except TypeError:
            print("Cannot add: some of your input data belong to a wrong type (not int nor float)")
    def subtract(self):
        try:
            return self.a - self.b
        except TypeError:
            print("Cannot subtract: some of your input data belong to a wrong type (not int nor float)")

    def multiple(self):
        try:
            return self.a * self.b
        except TypeError:
            print("Cannot multiply: some of your input data belong to a wrong type (not int nor float)")

    def divide(self):
        try:
            return self.a / self.b
        except ZeroDivisionError:
            print("Fortunately or unfortunately, but you cannot devide by a zero")
        except TypeError:
            print("Cannot devide: some of your input data belong to a wrong type (not int nor float)")
    def divide_v2(self):
        try:
            return int(self.a / self.b)
        except TypeError:
            print("Cannot devide: some of your input data belong to a wrong type (not int nor float)")
        except ZeroDivisionError:
            print("Fortunately or unfortunately, but you cannot devide by a zero")



proccess_input = ProcessInput(a='1.1', b=0)
print(proccess_input.add()) # выведет 30
print(proccess_input.subtract()) # выведет 10
print(proccess_input.multiple()) # выведет 200
print(proccess_input.divide()) # выведет 2
# because the 2.0 above is not the 2 indeed the following  method was added:
print(proccess_input.divide_v2()) # выведет 2
