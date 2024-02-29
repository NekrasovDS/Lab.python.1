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

#Функция 3.
def get_filename_without_extension(file_path):
    filename = os.path.basename(file_path)
    filename_without_extension = os.path.splitext(filename)[0]
    return filename_without_extension

#Ввод и вывод
number = int(input('Для решения определённой задачи, введите её номер (предложенные задачи варианта: 2, 10, 17): '))
if number == 2:
    text = input('Введите желаемую строку: ')
    result = find_lowercase_letters(text)
    print(result)
if number == 10:
    input_string = input('Введите желаемую строку: ')
    result = count_unique_latin_chars(input_string)
    print(result)
if number == 17:
    file_path = input('Введите путь: ')
    filename = get_filename_without_extension(file_path)
    print (filename)
