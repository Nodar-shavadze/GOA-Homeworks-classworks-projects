#1
def min_max(lst):
  return [min(lst), max(lst)]
#2 სრულად არ მუშაობს რატომღაც
def is_leap_year(year):
    if year //4:
        return(True)
    elif year // 400:
        return(True)
    elif year // 100:
        return False
    else:
        return(False)
#3
def fizzbuzz(n):
    list = []
    for i in range (1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            list.append("FizzBuzz")
        elif i % 3 == 0:
            list.append("Fizz")
        elif i % 5 == 0:
            list.append("Buzz")
        else:
            list.append(i)
    return list
#4 ვერ გავაკეთე

#5
def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    else:
        return "No"
#6
def remove_char(s):
    return s[1:-1]
#7
def count_sheeps(sheep):
    return sheep.count(True)
#8
def litres(time):
    return  int(time * 0.5)
    
#9
def paperwork(n, m):
    if n > 0 and m > 0:
        return n * m
    else:
        return 