"""
Обязательными будут задача 1 и 2, задачка 3 - когда скучно :)

# ЗАДАЧА-1
# Написать свой декоратор который будет проверять остаток от деления числа 100 на результат работы функции.
# Если остаток от деления = 0, вывести сообщение "We are OK!», иначе «Bad news guys, we got {}» остаток от деления.

# ЗАДАЧА-2
# Написать декоратор который будет выполнять предпроверку типа аргумента который передается в вашу функцию.
# Если это int, тогда выполнить функцию и вывести результат, если это str(),
# тогда зарейзить ошибку ValueError (raise ValueError(“string type is not supported”))

Привет, по поводу задачи 2 в декораторах. По условию вы должны там рейзить ошибку, не смущайтесь когда вылетит трейсбек
с ошибкой  ValueError: string type is not supported. Так и задуманно

Пример рейза ошибок:
try:
  f()
except ValueError:
  raise ValueError(“string type is not supported”)

# *ЗАДАЧА-3
# Написать декоратор который будет кешировать значения аргументов и результаты работы вашей функции и записывать
# его в переменную cache. Если аргумента нет в переменной cache и функция выполняется, вывести сообщение
# «Function executed with counter = {}, function result = {}» и количество раз сколько эта функция выполнялась.
# Если значение берется из переменной cache, вывести сообщение «Used cache with counter = {}» и
# количество раз обращений в cache.
"""

# ЗАДАЧА-1
# Написать свой декоратор который будет проверять остаток от деления числа 100 на результат работы функции.
# Если остаток от деления = 0, вывести сообщение "We are OK!», иначе «Bad news guys, we got {}» остаток от деления.


def decorator_division_reminder(division_reminder):
    def wrapper_around_original_function(*args, **kwargs):
        if division_reminder(*args, **kwargs) == 0:
            print("We are OK!")
        else:
            print(f"Bad news guys, we got {division_reminder(*args, **kwargs)}")

    return(wrapper_around_original_function)

@decorator_division_reminder
def division_reminder(dividend, divisor):
    """
    a test function to study decorators
    :param dividend: the number to be divided (e.g. 7 in 7 / 5)
    :param divisor: the number that divides (e.g. 5 in 7 / 5)
    :return: the remainder after dividing the dividend by the divisor (e.g. 2 in 7 / 5)
    """
    return dividend % divisor


# ЗАДАЧА-2
# Написать декоратор который будет выполнять предпроверку типа аргумента который передается в вашу функцию.
# Если это int, тогда выполнить функцию и вывести результат, если это str(),
# тогда зарейзить ошибку ValueError (raise ValueError(“string type is not supported”))

# Привет, по поводу задачи 2 в декораторах. По условию вы должны там рейзить ошибку, не смущайтесь когда вылетит трейсбек
# с ошибкой  ValueError: string type is not supported. Так и задуманно


def decorator_type_check(bulk_func):
    def wrapper_around_original_function(*args, **kwargs):
        pass
        if isinstance(args[0], str):
            print(bulk_func(*args, **kwargs))
        elif isinstance(args[0], int):
            raise ValueError("string type is not supported")
        else:
            print("it is not a string or a integer; I don't know what to do")

    return (wrapper_around_original_function)

@decorator_type_check
def bulk_func(a):
    """
    the function able to process both int and str
    :param a: some parameter
    :return: a*3
    """
    return a * 3

