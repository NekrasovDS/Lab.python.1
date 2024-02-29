#Задание 6-8. Вариант 8.
#Функция 1.
def find_lowercase_letters(text):
    lowercase_letters = set()
    for char in text:
        if char.islower():
            lowercase_letters.add(char)
    return lowercase_letters

#Функция 2.
def count_unique_latin_chars(input_string):
    latin_chars = set(char for char in input_string if char.isalpha() and char.isascii() and char.islower())
    return len(latin_chars)
