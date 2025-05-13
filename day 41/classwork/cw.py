
def max_multiple(divisor, bound):
    return bound - (bound % divisor)

#მეორე ვერ გავაკეთე :()

def dont_give_me_five(start, end):
    count = 0
    for num in range(start, end + 1):
        if '5' not in str(num):
            count += 1
    return count

def fizzbuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

def sum_array(arr):
    if not arr or len(arr) < 3:
        return 0
    total = sum(arr)
    total -= max(arr)
    total -= min(arr)
    return total