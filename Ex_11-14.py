#Вариант 8. Задание 11-14.
#Задача 2.
def sort_strings_by_avg_weight(strings):
    return sorted(strings, key=lambda x: sum(ord(char) for char in x)/len(x))

#Задача 4.
def sort_by_quadratic_deviation(strings):
    ref_avg = sum(ord(char) for char in strings[0])/len(strings[0])
    return sorted(strings, key=lambda x: (sum(ord(char) for char in x)/len(x) - ref_avg)**2)

