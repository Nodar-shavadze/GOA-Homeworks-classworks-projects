def greet(name):
    return f"Hello, {name}!"

def summation(num):
    return sum(range(1, num + 1))

def reverse_string(s):
    return s[::-1]

def remove_char(s):
    return s[1:-1]

def bool_to_word(boolean):
    return "Yes" if boolean else "No"

def count_sheep(n):
    return ''.join(f"{i} sheep..." for i in range(1, n + 1))

def make_negative(number):
    return -abs(number)