#Вариант 8. Задание 11-14.
#Задача 2.
def sort_strings_by_avg_weight(strings):
    return sorted(strings, key=lambda x: sum(ord(char) for char in x)/len(x))

#Задача 4.
def sort_by_quadratic_deviation(strings):
    ref_avg = sum(ord(char) for char in strings[0])/len(strings[0])
    return sorted(strings, key=lambda x: (sum(ord(char) for char in x)/len(x) - ref_avg)**2)

#Задача 8.
def mean_weight_ascii_deviation(s):
    mean_weight = sum(ord(c) for c in s)/len(s)
    ascii_codes = [ord(c) for c in s]

    max_three_consecutive_ascii = 0
    for i in range(len(ascii_codes) - 2):
        three_consecutive_ascii = sum(ascii_codes[i:i+3])
        max_three_consecutive_ascii = max(max_three_consecutive_ascii, three_consecutive_ascii)

    quadratic_deviation= (mean_weight - max_three_consecutive_ascii) ** 2
    return quadratic_deviation

#Задача 10.
def count_mirror_triples(s):
    count = 0
    for i in range(len(s) - 2):
        if s[i] == s[i+2] and s[i] != s[i+1]:
            count += 1
    return count

def sort_by_mirror_triples(strings):
    return sorted(strings, key=lambda x: count_mirror_triples(x))



