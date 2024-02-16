#Задание 2. Вариант 8.
#Задача 2.
def check_ordered(string):
    lowercase_chars = [char for char in string if char.islower()]
    sorted_chars = sorted(lowercase_chars)
    return lowercase_chars == sorted_chars

#Задача 10
def count_letter_A(string):
    count = 0
    for letter in string:
        if letter == 'A':
            count +=1
    return count
