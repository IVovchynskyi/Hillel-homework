"""
1) Дан массив чисел.
[10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
1.1) убрать из него повторяющиеся элементы
1.2) вывести 3 наибольших числа из исходного массива
1.3) вывести индекс минимального элемента массива
1.4) вывести исходный массив в обратном порядке

2) Сгенерировать массив(list()). Из диапазона чисел от 0 до 100 записать в результирующий массив только четные числа.

3) Найти общие ключи в двух словарях:
dict_one = { ‘a’: 1, ‘b’: 2, ‘c’: 3,  ‘d’: 4 }
dict_two = { ‘a’: 6,  ‘b’: 7, ‘z’: 20, ‘x’: 40 }

4) Сгенерировать dict() из списка ключей ниже по формуле (key : key* key).
keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ожидаемый результат: {1: 1, 2: 4, 3: 9 …}
"""

# 1.
InitialArray = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
# убрать из него повторяющиеся элементы
NoDuplicateArray = list(set(InitialArray))
# print(NoDuplicateArray)

# The function to check that we were right
def DuplicateInArray(TheArray):
    while bool(TheArray) is True:
        ComparisonTarget = TheArray.pop()
        # print (ComparisonTarget)
        # print(TheArray)
        for element in TheArray:
            # print(f"comparing {ComparisonTarget} with {element}")
            if ComparisonTarget == element:
                print(f"{ComparisonTarget} is the duplicate!")
                return
            # print("--------------")
    print("No duplicates were found")
# Checkign process
DuplicateInArray(InitialArray)


