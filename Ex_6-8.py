#Задание 6-8. Вариант 8.
#Функция 1.
def find_lowercase_letters(text):
    lowercase_letters = set()
    for char in text:
        if char.islower():
            lowercase_letters.add(char)
    return lowercase_letters
