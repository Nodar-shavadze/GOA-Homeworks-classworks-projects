#string repeat

def repeat_str(repeat, string):
   return(repeat*string)

#basic mathematical operations

def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    elif operator == "/":
        return value1 / value2
    else:
        return "Invalid operator"
    
#opposite number
def opposite(number):
    return -number

#century from year
def century(year):
    return (year + 99) // 100

#simple multiplication
def simple_multiplication(number):
    return number * 8 if number % 2 == 0 else number * 9


#volume of cuboid
def get_volume_of_cuboid(length, width, height):
    return length * width * height



my_list = [1, 2, 3, 4, 5]  # სია 5 ელემენტით
del my_list[2]             # მე-3 ელემენტის (ინდექსი 2) წაშლა
my_list.insert(0, "new")   # ახალი ელემენტის დამატება მე-0 ინდექსზე
print(my_list)             # შედეგის დაბრუნება


def power(base, exponent):
    return base ** exponent  # პირველი რიცხვის აყვანა მეორე რიცხვის ხარისხში

print(power(2, 3))  # Output: 8
print(power(5, 2))  # Output: 25



def check_list_length(lst):
    if len(lst) % 2 == 0:  # თუ სიის სიგრძე ლუწია
        return "List length is even"
    else:                  # სხვა შემთხვევაში
        return "List length is odd"

print(check_list_length([1, 2, 3, 4]))   # Output: List length is even
print(check_list_length([1, 2, 3]))      # Output: List length is odd
