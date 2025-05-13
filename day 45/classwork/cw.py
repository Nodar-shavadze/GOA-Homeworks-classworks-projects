#1---
def divisible_by(numbers, divisor):
    result = []
    for number in numbers:
        if number % divisor == 0:
            result.append(number)
    return result


#2----
def how_many_lightsabers_do_you_own(name):
    if name == "Zach":
        return 18
    else:
        return 0


#3---
def check_player_status(age, is_alive):
    if age < 18:
        if is_alive:
            return "You're too young to play."
        else:
            return "You're dead."
    else:
        if is_alive:
            return "You're old enough to play."
        else:
            return "You're dead."
#4---
def check_case(c1, c2):
    if not (c1.isalpha() and c2.isalpha()):
        return -1
    return 1 if c1.islower() == c2.islower() else 0


