# Задание 1. Вариант 8.
# Функция 1.
import math
def count_coprimes(n):
    count = 0
    for i in range(1, n):
        if math.gcd(i, n) == 1:
            count += 1
    return count

# Функция 2.
def sums_of_simple(number):
    sum_of_digits = 0
    while number > 0:
        digit = number % 10
        if digit % 3 == 0:
            sum_of_digits += digit
        number //= 10
    return sum_of_digits

# Функция 3.
import math
def sums_of_numbers(number):
    sum_of_digits = 0
    while number > 0:
        digit = number % 10
        sum_of_digits += digit
        number //= 10
    for i in range(2,sum_of_digits):
        if number % i == 0 and math.gcd(i, sum_of_digits) == 1:
            return i
