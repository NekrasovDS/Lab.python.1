#Задание 10.
strings = []
n = int(input("Введите количество строк: "))
for _ in range(n):
    strings.append(input("Введите строку: "))
sorted_strings = sorted(strings, key=lambda x: len(x.split()))
for string in sorted_strings:
    print(string)
