#len-გამოაქვს სიაში რამდენი ელემენტია
სია=["banana", "ice cream", "popcorn", "potato", "chips"]
სია.insert(4, "khinkali")
print(სია)

სია2 = ["banana", "ice cream", "popcorn", "potato", "chips"]
სია2.pop(0)
სია2.pop(4)
print(სია2)

სია3=[ "banana", "ice cream", "popcorn", "potato", "chips", "khinkali", "khachapuri", "vashi", "soko", "msxali" ]

user_input=int(input("type number 0-9"))
სია3.pop(user_input)

name_input=input("name: ")
if name_input > 5:
    print("hello")
else:
    print("bye")
