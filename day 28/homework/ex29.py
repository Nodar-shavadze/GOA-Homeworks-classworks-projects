# 1. ფუნქცია რომელიც რიცხვების ნამრავლს ბეჭდავს
def multiply_numbers(a, b):
    print("The product of", a, "and", b, "is:", a * b)

# მაგალითი გამოძახება:
multiply_numbers(3, 5)


# 2. ფუნქცია, რომელიც აბრუნებს რიცხვის ლუწობას ან კენტობას
def is_even_or_odd(number):
    if number % 2 == 0:
        return str(number) + " is even"
    else:
        return str(number) + " is odd"

# მაგალითი გამოძახება:
print(is_even_or_odd(4))
print(is_even_or_odd(7))


# 3. ფუნქცია, რომელიც სახელს მიესალმება
def greet(name):
    print("Hello " + name + "!")

# მაგალითი გამოძახება:
greet("Giorgi")
greet("Nodar")


# 4. ფუნქცია, რომელიც ორი სტრინგის კონკატენაციას აკეთებს
def concatenate_strings(string1, string2):
    return string1 + string2

# მაგალითი გამოძახება:
result = concatenate_strings("Hello, ", "World!")
print(result)
