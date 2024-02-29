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

def get_filename_without_extension(file_path):
    filename = os.path.basename(file_path)
    filename_without_extension = os.path.splitext(filename)[0]
    return filename_without_extension

number = int(input('Для решения определённой задачи, введите её номер (предложенные задачи варианта: 2, 10, 17): '))
if number == 2:
    string = input('Введите желаемую строку: ')
    ordered = check_ordered(string)
    print(ordered)
if number == 10:
    string = input('Введите желаемую строку: ')
    a_count = count_letter_A(string)
    print(a_count)
if number == 17:
    file_path = input('Введите путь: ')
    filename = get_filename_without_extension(file_path)
    print (filename)
