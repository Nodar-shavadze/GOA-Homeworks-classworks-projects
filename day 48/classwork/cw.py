def replace_exclamation(s):
    return ''.join('!' if c.lower() in 'aeiou' else c for c in s)

def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())

def sp_eng(sentence):
    return 'english' in sentence.lower()

def cookie(x):
    if isinstance(x, str):
        return "Who ate the last cookie? It was Zach!"
    elif isinstance(x, (int, float)):
        return "Who ate the last cookie? It was Monica!"
    else:
        return "Who ate the last cookie? It was the dog!"

def sum_str(a, b):
    return str(int(a or 0) + int(b or 0))

def whatday(num):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    return days[num - 1] if 1 <= num <= 7 else "Wrong, please enter a number between 1 and 7"

def swap(string_):
    return ''.join(c.upper() if c.islower() else c.lower() for c in string_)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def zip_with(fn, a1, a2):
    return [fn(a, b) for a, b in zip(a1, a2)]