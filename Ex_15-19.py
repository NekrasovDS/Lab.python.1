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


