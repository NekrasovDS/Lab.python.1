#Задание 9.
strings_list = []
n = int(input("Введите количество строк: "))
for _ in range(n):
    strings_list.append(input("Введите строку: "))
sorted_strings = sorted(strings_list, key=len)
print(sorted_strings)
