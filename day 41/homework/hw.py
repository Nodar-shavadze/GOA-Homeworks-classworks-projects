def modify_case(name):
    result = ''
    for i in range(len(name)):
        if i % 2 == 0:
            result += name[i].upper()
        else:
            result += name[i].lower()
    return result

def manual_join(iterable):
    result = ''
    for item in iterable:
        result += item
    return result

correct_email = 'example@example.com'
correct_password = 'securepassword123'

while True:
    email = input('შეიყვანეთ ელ. ფოსტა: ')
    password = input('შეიყვანეთ პაროლი: ')
    if email == correct_email and password == correct_password:
        print('მომხმარებელი წარმატებით ავტორიზებულია.')
        
    else:
        print('ელ. ფოსტა ან პაროლი არასწორია. სცადეთ თავიდან.')
