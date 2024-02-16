#Задание 2. Вариант 8.
#Задача 2.
def check_ordered(string):
    lowercase_chars = [char for char in string if char.islower()]
    sorted_chars = sorted(lowercase_chars)
    return lowercase_chars == sorted_chars


