#Вариант 8. Задания 15-19.
#Задача 8.
def find_two_min_indices(arr):
  min1 = min(arr)
  min1_index = arr.index(min1)
  arr[min1_index] = float('inf')
  min2 = min(arr)
  min2_index = arr.index(min2)
  return min1_index, min2_index

#Задача 20.
def find_missing_numbers(arr):
  n = len(arr)
  missing = []
  for i in range(1, n+1):
    if i not in arr:
      missing.append(i)
  return missing

#Задача 32.
def count_local_maxima(arr):
  count = 0
  for i in range(1, len(arr) - 1):
    if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
      count += 1
return count

#Задача 45.
def check_numbers(array):
  if len(array) < 2:
    return False

  for i in range(1, len(array)):
    if (isinstance(array[i-1], int) and isinstance(array[i], int)) or (isinstance(array[i-1], float) and isinstance(array[i], float)):
      return False
  return True

#Задача 56.
def average_of_non_primes_above_avg_of_primes(lst):
  primes = [num for num in lst if is_prime(num)]
  non_primes = [num for num in lst if not is_prime(num)]
  avg_primes = sum(primes) / len(primes) if primes else 0
  avg_non_primes = sum(num for num in non_primes if num > avg_primes) / len([num for num in non_primes if num > avg_primes]) if any(num > avg_primes for num in non_primes) else 0
  return avg_non_primes

