def remove_smallest(numbers):
    numbers.remove(min(numbers))
    return numbers

def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]

def count_divisors(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    return count

def reverse_string(s):
    return s[::-1]

def boolean_to_string(b):
    return str(b)

def make_negative(number):
    return -abs(number)

def double_char(s):
    return ''.join([char*2 for char in s])

def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2

def is_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

def no_space(s):
    return s.replace(" ", "")


