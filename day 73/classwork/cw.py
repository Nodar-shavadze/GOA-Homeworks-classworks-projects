#1
def printer_error(s):
    errors = 0
    
    for i in s:
        if i <"a" or i > "m":
            errors += 1
    return f"{errors}/{len(s)}" 
#3
def dont_give_me_five(start, end):
    count = 0
    for number in range(start, end + 1):
        if '5' not in str(number):
            count += 1
    return count
#-------------------------------------------------\
#1
def digital_root(n):
    while n > 9:
        numbers= str(n)
        total =0
        for i in numbers :
            total=total+int(i)
        n = total
    return n
#2