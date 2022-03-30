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
    Vowels = ("A", "E", "I", "O", "U")
    Consonants = (
    "B", "C", "D", "F", "G", "J", "K", "L", "M", "N", "P", "Q", "S", "T", "V", "X", "Z", "H", "R", "W", "Y")
    list_to_join = []
    for letter in list(the_string.upper()):
        if letter in Consonants:  # check for consonants
            list_to_join.append(random.choice(Vowels))  # change a consonant to a random vowel and add to the list
        else:  # not-consonant just go through
            list_to_join.append(letter)  # add them to the list
    return ("".join(list_to_join))  # transfer produced list back to string


print("""#1
Option 1
(!) This solution was made before any hints""")
print("Here it was: ", random_line)
print("Here it became: ", consonants_to_vowels_1(random_line))

