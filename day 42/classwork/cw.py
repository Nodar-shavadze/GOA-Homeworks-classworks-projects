def modify_name(name):
    result = ""
    for i, char in enumerate(name):
        if i % 2 == 0:  
            result += char.upper()
        else: 
            result += char.lower()
    return result

def manual_join(iterable, separator=""):
    result = ""
    for i, item in enumerate(iterable):
        result += item
        if i < len(iterable) - 1:  
            result += separator
    return result

def check_email_password():
    correct_email = "user@example.com"
    correct_password = "password123"
    
    while True:
        email = input("შეიყვანეთ თქვენი ემაილი: ")
        password = input("შეიყვანეთ თქვენი პაროლი: ")
        
        if email == correct_email and password == correct_password:
            print("შესვლა წარმატებით განხორციელდა!")
            
        else:
            print("ემაილი ან პაროლი არასწორია. სცადეთ ხელახლა.")




name = "nOdOdEmO"
print(modify_name(name))  


items = ["Hello", "World", "Python"]
print(manual_join(items, ", ")) 

check_email_password()
