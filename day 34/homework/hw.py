""""""
def maskify(string):
    
    if len(string) <= 4:
        return string
    else:
       
        return "#" * (len(string) - 4) + string[-4:]
    
""""""
def solution(string, ending):
    return string.endswith(ending)
""""""
def remove_url_anchor(url):
    return url.split('#')[0]
""""""
def capitals(word):
    return [i for i, char in enumerate(word) if char.isupper()]
""""""
def sum_cubes(n):
    return (n * (n + 1) // 2) ** 2
""""""
def solution(nums):
    if nums is None:
        return []
    return sorted(nums)
""""""
def max_multiple(divisor, bound):
    return bound - (bound % divisor)
""""""
def sum_digits(number):
    return sum(int(digit) for digit in str(abs(number)))
""""""
def dont_give_me_five(start, end):
    count = 0
    for number in range(start, end + 1):
        if '5' not in str(number):
            count += 1
    return count
""""""
def fizzbuzz(n):
    return [
        "FizzBuzz" if i % 3 == 0 and i % 5 == 0 else
        "Fizz" if i % 3 == 0 else
        "Buzz" if i % 5 == 0 else
        i  
        for i in range(1, n + 1)
    ]
""""""
def invert(lst):
    return [-x for x in lst]
""""""
def sum_array(arr):
    if arr is None or len(arr) <= 2:
        return 0
    arr.remove(max(arr))
    arr.remove(min(arr))
    return sum(arr)
""""""
def manual_split(string, delimiter):
    result = []
    current_word = ""
    for char in string:
        if char == delimiter:
            if current_word:  
                result.append(current_word)
            current_word = ""  
        else:
            current_word += char  
    if current_word: 
        result.append(current_word)
    return result


""""""



def manual_replace(string, old, new):
    result = ""
    i = 0
    while i < len(string):
        if string[i:i+len(old)] == old:
            result += new
            i += len(old)  
        else:
            result += string[i]
            i += 1
    return result



def manual_join(lst, delimiter):
    result = ""
    for i in range(len(lst)):
        result += lst[i]
        if i != len(lst) - 1:  
            result += delimiter
    return result





