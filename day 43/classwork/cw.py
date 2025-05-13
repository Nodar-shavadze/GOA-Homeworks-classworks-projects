def divisible_by(numbers, divisor):
    result = []
    for n in numbers:
        if n % divisor == 0:
            result.append(n)
    return result

def how_many_times(annual_price, individual_price):
    return annual_price // individual_price

def get_military_time(time):
    if time[-2:] == "AM":
        if time[:2] == "12":
            return "00" + time[2:-2]
        else:
            return time[:-2]
    else:
        if time[:2] == "12":
            return time[:-2]
        else:
            return str(int(time[:2]) + 12) + time[2:8]

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def same_case(a, b):
    if not a.isalpha() or not b.isalpha():
        return -1
    if (a.islower() and b.islower()) or (a.isupper() and b.isupper()):
        return 1
    return 0

def swap(string_):
    result = ""
    for char in string_:
        if char.islower():
            result += char.upper()
        else:
            result += char.lower()
    return result