# 1) გადააქციეთ string "hello" დიდ ასოებად .upper()-ის გამოყენებით
string1 = "hello"
print(string1.upper())  # Output: "HELLO"

# 2) გადააქციეთ string "GOA" პატარა ასოებად .lower()-ის გამოყენებით
string2 = "GOA"
print(string2.lower())  # Output: "goa"

# 3) გამოიყენეთ ფუნქცია .capitalize() სტრინგზე: "georgia"
string3 = "georgia"
print(string3.capitalize())  # Output: "Georgia"

# 4) string "hello" - ში მოძებნეთ ასობგერა "d" და დაპრინტეთ მისი ინდექსი
# Explanation: სტრინგში "hello" ასობგერა "d" არ არსებობს, ამიტომ გამოიტანს ერორს.
string4 = "hello"
# print(string4.index("d"))  # Error: ValueError: substring not found

# 5) string "GOA" - ში მოძებნეთ ასობგერა "A" და დაპრინტეთ მისი ინდექსი
string5 = "GOA"
print(string5.index("A"))  # Output: 2
