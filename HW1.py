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
# 1.1) убрать из него повторяющиеся элементы
NoDuplicateArray = list(set(InitialArray))
print(NoDuplicateArray)

# The function to check that we were right
def FindDuplicateInArray(TheArray):
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
# FindDuplicateInArray(NoDuplicateArray)

# 1.2) вывести 3 наибольших числа из исходного массива
def NMaxElents(HowManyElements, TheArray):
    MaxNumbersList = []
    NoDuplicateArray = list(set(TheArray))  # to avoid the "76, 76, 43" answer
    while bool(HowManyElements) is True:
        HowManyElements -= 1
        MaxNumbersList.append(max(NoDuplicateArray))
        NoDuplicateArray.remove(max(NoDuplicateArray))
    return(print(MaxNumbersList))

NMaxElents(3, InitialArray)

# 1.3) вывести индекс минимального элемента массива
def ShowMinIndexOfArray(TheArray):
    MinValueInArray = min(TheArray)
    TargetElementQty = TheArray.count(MinValueInArray)
    if TargetElementQty == 1:
        MinIndex = TheArray.index(MinValueInArray)
        return(print(MinIndex))
    else: # .count shouldn't return a negative value, so no extra 'if > 1' needed
        return(print("There are several indexes of the minimal element; it is out of the current scope!"))

        """ Possible solution of the multiple minimal elements in the array
        MinIndexList
        while bool(TargetElementQty) = True
        TargetElementQty -= 1
        MinIndex = TheArray.index(MinValueInArray)
        MinIndexList.append(MinIndex)
        0) we cannot just `TheArray.remove(MinValueInArray)` or `TheArray.pop(MinIndex)`
        because indexes after the first one will be shifted (#2 by 1, #3 by 2, et.c.) 
        1) So we need to make a correction fro this shift
        2) OR to replace already found positions by unique values (ideally not from TheArray, but at least any != MinValueInArray)
        """

ShowMinIndexOfArray(InitialArray)

