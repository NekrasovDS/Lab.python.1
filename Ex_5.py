#Задание 5.

import re

text = input("Введите текст: ")
dates = re.findall(r'\d{1,2} [а-яА-Я]+ \d{4}', text)

for date in dates:
    print(date)
