
def make_negative(number):
    return -abs(number)


def number_to_string(num):
    return str(num)



def solution(string):
    return string[::-1]



def remove_char(s):
    return s[1:-1]



def positive_sum(arr):
    return sum(x for x in arr if x > 0)




def opposite(number):
    return -number


def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"


def get_count(sentence):
    return sum(1 for char in sentence if char in 'aeiouAEIOU')



def abbrev_name(name):
    return '.'.join([part[0].upper() for part in name.split()])



def multiply(a, b):
    return a * b