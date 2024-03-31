# Вариант 8. Задания 15-19.
# Задача 8.
def find_two_min_indices(arr):
    min1 = min(arr)
    min1_index = arr.index(min1)
    arr[min1_index] = float('inf')
    min2 = min(arr)
    min2_index = arr.index(min2)
    return min1_index, min2_index


# Задача 20.
def find_missing_numbers(arr):
    n = len(arr)
    missing = []
    for i in range(1, n + 1):
        if i not in arr:
            missing.append(i)
    return missing


# Задача 32.
def count_local_maxima(arr):
    count = 0
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            count += 1
    return count


# Задача 45.
def sum_elements_in_range(arr, a, b):
    return sum(x for x in arr if a <= x <= b)


# Задача 56.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def average_of_non_primes_above_avg_of_primes(lst):
    primes = [num for num in lst if is_prime(num)]
    non_primes = [num for num in lst if not is_prime(num)]
    avg_primes = sum(primes) / len(primes) if primes else 0
    avg_non_primes = sum(num for num in non_primes if num > avg_primes) / len(
        [num for num in non_primes if num > avg_primes]) if any(num > avg_primes for num in non_primes) else 0
    return avg_non_primes


# Ввод и вывод
number = int(input('Для решения определённой задачи, введите её номер (предложенные задачи варианта: 8, 20, 32, 45, 56): '))
if number == 8:
    ordered = list(map(int, input('Введите массив чисел через пробел: ').split()))
    result = find_two_min_indices(ordered)
    print(result)
if number == 20:
    ordered = list(map(int, input('Введите массив чисел через пробел: ').split()))
    result = find_missing_numbers(ordered)
    print(result)
if number == 32:
    ordered = list(map(int, input('Введите массив чисел через пробел: ').split()))
    result = count_local_maxima(ordered)
    print(result)
if number == 45:
    ordered = list(map(int, input('Введите массив чисел через пробел: ').split()))
    interval_a = int(input('Введите a: '))
    interval_b = int(input('Введите b: '))
    result = sum_elements_in_range(ordered, interval_a, interval_b)
    print(result)
if number == 56:
    ordered = list(map(int, input('Введите массив чисел через пробел: ').split()))
    result = average_of_non_primes_above_avg_of_primes(ordered)
    print(result)
