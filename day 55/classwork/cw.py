#2
def are_you_playing_banjo(name):
    if name[0].lower() == "r":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
#3 
def simple_multiplication(number):
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9
#6
def disemvowel(string):
    aeiou = "aeiou"
    for i in aeiou:
        string = string.replace(i, "")
        string = string.replace(i.upper(),"")
    return string