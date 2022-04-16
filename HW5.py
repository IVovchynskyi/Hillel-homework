"""
1) Реализовать класс который бы производил разные операции над 2мя переданными числами.

Пример Использования:

proccess_input = ProcessInput(a=20, b=10)
print(proccess_input.add()). # выведет 30
print(proccess_input.subtract()). # выведет 10
print(proccess_input.multiple()). # выведет 200
print(proccess_input.divide()). # выведет 2
"""


class ProcessInput:
    """
    the class to perform some actions with two input digits
    """

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiple(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b

    def divide_v2(self):
        return int(self.a / self.b)



proccess_input = ProcessInput(a=20, b=10)
print(proccess_input.add()) # выведет 30
print(proccess_input.subtract()) # выведет 10
print(proccess_input.multiple()) # выведет 200
print(proccess_input.divide()) # выведет 2
# because the 2.0 above is not the 2 indeed the following  method was added:
print(proccess_input.divide_v2()) # выведет 2
