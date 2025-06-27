import re

def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        return [1, 15, 15]
    elif human_years == 2:
        return [2, 24, 24]
    else:
        return [human_years, 24 + (human_years - 2) * 4, 24 + (human_years - 2) * 5]

def triangular(n):
    return n * (n + 1) // 2 if n > 0 else 0

def lucky_number(n):
    return int(''.join(sorted(str(n), reverse=True)))

def coffee_time(s):
    return s.lower().count('coffee') * 2

def calculate_total_reps(reps):
    return sum(reps)

def pig_it(text):
    return ' '.join(word[1:] + word[0] + 'ay' if word.isalpha() else word for word in text.split())

def how_many_petals(nb_petals):
    phrases = [
        "I love you", "a little", "a lot", "passionately", "madly", "not at all"
    ]
    return phrases[(nb_petals - 1) % 6]

def variable_name(name):
    return bool(re.match(r'^[a-zA-Z_]\w*$', name))

