#1
def disemvowel(string_):
    result = ""
    vowels = "aeiouAEIOU"
    for letter in string_:
        if letter not in vowels:
            result += letter
    return result
#2
def maskify(string):
    if len(string) <= 4:
        return string
    else:
        return "#" * (len(string) - 4) + string[-4:]
#3

def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())
#4
def solution(string, ending):
    return string.endswith(ending)
#5
def is_isogram(string):
    string = string.lower()
    return len(string) == len(set(string))
#6
def count_sheep(n):
    return sum(1 for i in range(1, n + 1) if i % 2 == 0)
#7
def sum_two_smallest_numbers(numbers):
    sorted_numbers = sorted(numbers)
    return sorted_numbers[0] + sorted_numbers[1]
#8
def printer_error(s):
    errors = 0
    
    for i in s:
        if i <"a" or i > "m":
            errors += 1
    return f"{errors}/{len(s)}" 


