"""
Please wrap all logic in functions:
1) Заменить в произвольной строке согласные буквы на гласные.
2) Дан массив из словарей
data = [
  {'name': 'Viktor', 'city': 'Kiev', 'age': 30 },
  {'name': 'Maksim', 'city': 'Dnepr', 'age': 20},
  {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},
  {'name': 'Andrey', 'city': 'Kiev', 'age': 34},
  {'name': 'Artem', 'city': 'Dnepr', 'age': 50},
  {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}]

2.1) отсортировать массив из словарей по значению ключа ‘age'
2.2) сгруппировать данные по значению ключа 'city'
вывод должен быть такого вида :
result = {
  'Kiev': [
   {'name': 'Viktor', 'age': 30 },
   {'name': 'Andrey', 'age': 34}],

  'Dnepr': [ {'name': 'Maksim', 'age': 20 },
       {'name': 'Artem', 'age': 50}],
  'Lviv': [ {'name': 'Vladimir', 'age': 32 },
       {'name': 'Dmitriy', 'age': 21}]
}
3) У вас есть последовательность строк. Необходимо определить наиболее часто встречающуюся строку в последовательности.
Например:

def most_frequent(list_var):
  #your code is here
  return

most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
"""

# 1) Заменить в произвольной строке согласные буквы на гласные.

random_line = 'The quick brown fox jumps over the lazy dog'


def consonants_to_vowels_1(the_string):
    """
    Changes a consonant to a random vowel in string
    :return: returns initial string and the string with consonant changed to vowels
    """
    import random
    VOWELS = ("A", "E", "I", "O", "U")
    CONSONANTS = (
    "B", "C", "D", "F", "G", "J", "K", "L", "M", "N", "P", "Q", "S", "T", "V", "X", "Z", "H", "R", "W", "Y")
    list_to_join = []
    for letter in list(the_string.upper()):
        if letter in CONSONANTS:  # check for consonants
            list_to_join.append(random.choice(VOWELS))  # change a consonant to a random vowel and add to the list
        else:  # not-consonant just go through
            list_to_join.append(letter)  # add them to the list
    return "".join(list_to_join)  # transfer produced list back to string


print("""#1
Option 1
(!) This solution was made before any hints""")
print("Here it was: ", random_line)
print("Here it became: ", consonants_to_vowels_1(random_line))


consonants = "bcdfghjklmnpqrstvwxyz"
vowels = "aeiou"

def consonants_to_vowels_2(the_string):
    import random
    for the_consonant in consonants:
        # print(the_string)
        the_string = the_string.lower().replace(the_consonant, random.choice(vowels), random_line.count(the_consonant))
    return the_string

print("""#1
Option 2
The option 2 was made after I heard about the find(), so I decided to use it
I still think that the first option is better because it "picks up" the string less times""")
print("Here it was: ", random_line)
print("Here it became: ", consonants_to_vowels_2(random_line))

# 3) У вас есть последовательность строк. Необходимо определить наиболее часто встречающуюся строку в последовательности.
# most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'

# сделать функцию генератор входных данных
# количество стрингов: конкретное значение или от X до Y
# длина стрингов:  конкретное значение или от X до Y

def third_task_input_generator(total_min_qty, total_max_qty, string_min_length, string_max_length, string_min_iteration, string_max_iteration):
    """
    generates list of strings with defined length and qty limitations; all generated strings should be placed randomly
    into the output list
    :param total_min_qty: minimal qty of strings (how many strings in general do we need)
    :param total_max_qty: maximal qty of strings (how many strings in general do we need)
    :param string_min_iteration: minimal qty of strings (how many strings copies are allowed)
    :param string_max_iteration: maximal qty of strings (how many strings copies are allowed)
    :param string_min_length: minimal string_min_length of strings
    :param string_max_length: maximal string_min_length of strings
    :return:list of generated strings
    """
    # initial checking
    # (!) YES it is shitty, I should add some functions here to avoid copying the same code, but it is 2AM and I'm tired as f*ck
    if total_min_qty <= 0:
        print(f"\r\nMIN qty ({total_min_qty}) cannot be negative or equal to 0")
        return
    if total_min_qty > total_max_qty:
        print(f"\r\nMIN ({total_min_qty}) cannot be bigger than MAX({total_max_qty}); watch requested string qty!")
        return
    if string_min_length <= 0:
        print(f"\r\nMIN length ({string_min_length}) cannot be negative or equal to 0")
        return
    if string_min_length > string_max_length:
        print(f"\r\nMIN ({string_min_length}) cannot be bigger than MAX ({string_max_length})")
        return
    if string_min_iteration <= 0:
        print(f"\r\nMIN iteration number ({string_min_iteration}) cannot be negative or equal to 0")
        return
    if string_min_iteration > string_max_iteration:
        print(f"\r\nMIN ({string_min_iteration}) cannot be bigger than MAX ({string_max_iteration})")
        return

    # let's generate necessary variables from the obtained input
    the_output_list = []
    import random, string
    string_qty = random.randint(total_min_qty, total_max_qty)
    # print(f"randomized total number of strings is {string_qty}")
    while string_qty:
        string_qty -= 1
        # the one below seems to be an extra variable, but it makes understanding much easier
        current_string_length = random.randint(string_min_length, string_max_length)
        current_string = "".join(random.choices(string.ascii_letters + string.digits, k = current_string_length))
        # print(f"with length of {current_string_length} the string is {current_string}")
        # let's randomly insert (yes, for the first string is it useless, but all after it is good)
        # the one below seems to be an extra variable, but it makes understanding much easier
        iteration_qty = random.randint(string_min_iteration, string_max_iteration)
        # print(f"randomized iteration qty is {iteration_qty}")
        while iteration_qty:
            iteration_qty -= 1
            # the one below is complitely extra; i just want to have nice print() for refactoring
            if len(the_output_list) == 0:
                insert_position = 0
            else:
                insert_position = random.randint(0, len(the_output_list) - 1)
            the_output_list.insert(insert_position, current_string)
            # print(f"The string {current_string} is inserted to {insert_position}; iterations left {iteration_qty}")
            # print(f"output now is {the_output_list}")
    return(the_output_list)
# third_task_input_generator(2, 5, 3, 7, 2, 6)

#3
def most_frequent(the_list):
    # let's do it via dicts because we might need to show more detailed statistics in future
    pass

input_list = third_task_input_generator(3, 5, 3, 6, 4, 7)
# print(input_list)
count_dict = dict.fromkeys(set(input_list)) # all unique strings are dict keys now
for key in count_dict.keys(): # in other words: by every unique string of the list
    # string_qty = input_list.count(key)
    # print(f"the string {key} was found {string_qty} times")
    # according to https://stackoverflow.com/questions/15456158/python-dict-update-vs-subscript-to-add-a-single-key-value-pair
    #-> dict["key"] = value is faster than dict.update({"key":value})
    count_dict[key] = input_list.count(key)
# print(count_dict)
the_biggest_value = max(count_dict.values())
the_biggest_value_qty = list(count_dict.values()).count(the_biggest_value)
if the_biggest_value_qty > 1:
    print(f"There are several ({the_biggest_value_qty}) strings with the most often value ({the_biggest_value}):")
else:
    print(f"there is the only one string with the most often value ({the_biggest_value}):")
for key, value in count_dict.items():
    if value == the_biggest_value:
        print(key)
