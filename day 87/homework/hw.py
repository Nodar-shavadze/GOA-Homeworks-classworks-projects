# 8 kyu tasks

# 1. Convert a Number to a String!
def number_to_string(num):
    return str(num)

# 2. Opposite number
def opposite(number):
    return -number

# 3. Even or Odd
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# 4. Return Negative
def make_negative(number):
    return -abs(number)

# 5. Sum of positive
def positive_sum(arr):
    total = 0
    for x in arr:
        if x > 0:
            total += x
    return total

# 7 kyu tasks

# 1. Vowel Count
def get_count(sentence):
    count = 0
    for c in sentence:
        if c in 'aeiou':
            count += 1
    return count

# 2. Square Every Digit
def square_digits(num):
    result = ''
    for d in str(num):
        result += str(int(d) ** 2)
    return int(result)

# 3. Highest and Lowest
def high_and_low(numbers):
    nums = []
    for n in numbers.split():
        nums.append(int(n))
    return f"{max(nums)} {min(nums)}"

# 4. Disemvowel Trolls
def disemvowel(string_):
    result = ''
    for c in string_:
        if c.lower() not in 'aeiou':
            result += c
    return result

# 5. Mumbling
def accum(s):
    result = []
    for i, c in enumerate(s):
        result.append((c * (i+1)).capitalize())
    return '-'.join(result)

# 6 kyu tasks

# 1. Who likes it?
def likes(names):
    n = len(names)
    if n == 0:
        return "no one likes this"
    elif n == 1:
        return f"{names[0]} likes this"
    elif n == 2:
        return f"{names[0]} and {names[1]} like this"
    elif n == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {n-2} others like this"

# 2. Find the odd int
def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i