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
initial_array = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
# 1.1) убрать из него повторяющиеся элементы
no_duplicate_array = list(set(initial_array))
print("1.1 No duplicates array")
print(no_duplicate_array)

# The function to check that we were right
def find_duplicates_in_array(the_array):
    while the_array:
        comparison_target = the_array.pop()
        # print (comparison_target)
        # print(the_array)
        for element in the_array:
            # print(f"comparing {comparison_target} with {element}")
            if comparison_target == element:
                print(f"{comparison_target} is the duplicate!")
                return
            # print("--------------")
    print("No duplicates were found")
# find_duplicates_in_array(no_duplicate_array)

# 1.2) вывести 3 наибольших числа из исходного массива
def n_max_elents(how_many_elements, the_array):
    max_numbers_list = []
    no_duplicate_array = list(set(the_array))  # to avoid the "76, 76, 43" answer
    while how_many_elements:
        how_many_elements -= 1
        max_numbers_list.append(max(no_duplicate_array))
        no_duplicate_array.remove(max(no_duplicate_array))
    return(print(max_numbers_list))
print("1.2 Three max values of the array")
n_max_elents(3, initial_array)

# teacher's variant
sorted_list = sorted(no_duplicate_array, reverse=True)
print("Teacher's variant", sorted_list[:3])


# 1.3) вывести индекс минимального элемента массива
def show_min_index_of_array(the_array):
    min_valueIn_array = min(the_array)
    target_element_qty = the_array.count(min_valueIn_array)
    if target_element_qty == 1:
        min_index = the_array.index(min_valueIn_array)
        return(print(min_index))
    else: # .count shouldn't return a negative value, so no extra 'if > 1' needed
        return(print("There are several indexes of the minimal element; it is out of the current scope!"))

        """ Possible solution of the multiple minimal elements in the array
        min_indexList
        while target_element_qty:
        target_element_qty -= 1
        min_index = the_array.index(min_valueIn_array)
        min_indexList.append(min_index)
        0) we cannot just `the_array.remove(min_valueIn_array)` or `the_array.pop(min_index)`
        because indexes after the first one will be shifted (#2 by 1, #3 by 2, et.c.) 
        1) So we need to make a correction fro this shift
        2) OR to replace already found positions by unique values (ideally not from the_array, but at least any != min_valueIn_array)
        """
print("1.3 The index of the smallest value of the array")
show_min_index_of_array(initial_array)
# Teacher's answer
print("Teacher's answer", initial_array.index(min(initial_array)))
#1.4) вывести исходный массив в обратном порядке
# Option 1
initial_array.reverse()
print("1.4 reversed array; Option 1")
print(initial_array)
initial_array.reverse() # don't forget to change it back!
# Option 2
reversed_initial_array = list(reversed(initial_array))
print("1.4 reversed array; Option 2")
print(reversed_initial_array)
# Option 3
print("1.4 reversed array; Option 3")
print(initial_array[::-1])

#2) Сгенерировать массив(list()). Из диапазона чисел от 0 до 100 записать в результирующий массив только четные числа.
def even_array_generator(start, finish):
    even_array = []
    for i in range(start, finish + 1, 1):
        if i % 2 == 0:
            even_array.append(i)
    return(even_array)
even_array_generator(0,100)
print("2. Only even array from 0 to 100")
print(even_array_generator(0,100))
# Teacher's answer
print("Teacher's answer ", [i for i in range(100) if i % 2 == 0])

# 3) Найти общие ключи в двух словарях:
dict_one = { 'a': 1, 'b': 2, 'c': 3,  'd': 4 }
dict_two = { 'a': 6,  'b': 7, 'z': 20, 'x': 40 }
def same_keys_two_dicts(dict_one, dict_two):
    dict_one_keys = dict_one.keys()
    dict_two_keys = dict_two.keys()
    same_keys = []
    for compare_item in dict_one_keys:
        for target_item in dict_two_keys:
            if compare_item == target_item:
                same_keys.append(compare_item)
    return(same_keys)
print("3. The same keys of two dictioanaries")
print(same_keys_two_dicts(dict_one, dict_two))

# 4) Сгенерировать dict() из списка ключей ниже по формуле (key : key* key).
# keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# ожидаемый результат: {1: 1, 2: 4, 3: 9 …}

keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def square_dict_from_keys_list(keys):
    values = []
    for key in keys:
        value = key ** 2
        values.append(value)
    square_dict = dict(zip(keys, values))
    return(square_dict)
print("4. Dict with value = key ** 2")
print(square_dict_from_keys_list(keys))
# Teacher's answer
print("Teacher's answer ", {i: i*i for i in keys})

