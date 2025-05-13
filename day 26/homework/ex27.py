odd_numbers = []
for i in range(101):
    if i % 2 != 0:
        odd_numbers.append(i)
print("Odd numbers from 0 to 100:", odd_numbers)

foods = []
for i in range(5):
    food = input(f"Enter favorite food {i+1}: ")
    foods.append(food)

index = int(input("Enter an index to view and remove: "))
print("Food at index:", foods[index])
foods.pop(index)
print("Updated food list:", foods)

name_list = []
name = input("Enter your name: ")
change = input("How do you want to change it? (upper/lower/capitalize): ")

if change == "upper":
    name_list.append(name.upper())
elif change == "lower":
    name_list.append(name.lower())
elif change == "capitalize":
    name_list.append(name.capitalize())

print("Updated name list:", name_list)

name = input("Enter your name: ")
if len(name) >= 6:
    print("Hello")
elif len(name) == 5:
    print("Ola")
else:
    print("Bonju")

odd = []
even = []
for i in range(101):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even numbers:", even)
print("Odd numbers:", odd)

food_list = ["Pizza", "Burger", "Pasta", "Salad", "Sushi"]
fav_food = input("Enter your favorite food: ")
index = int(input("Enter an index to insert: "))

if 0 <= index < len(food_list):
    food_list.insert(index, fav_food)
else:
    print("Invalid index!")

print("Updated food list:", food_list)
