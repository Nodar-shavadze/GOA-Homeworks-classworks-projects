#2
def find_needle(haystack):
    i = 0
    for item in haystack:
        if item == "needle":
            return f"found the needle at position {i}"
        i += 1

#3
def grow(arr):
    result = 1  
    for i in arr:
        result = result * i 
    return result  


#4
def rental_car_cost(d):
    cost = d * 40
    if d >= 7:
        cost -= 50
    elif d >= 3:
        cost -= 20
    return cost

#6
def stray(numbers):
    for i in numbers:
        if numbers.count(i) == 1:
            return i

#7
def repeats(arr):
    result = 0
    for i in arr:
        if arr.count(i) == 1:
            result += i
    return result

#8