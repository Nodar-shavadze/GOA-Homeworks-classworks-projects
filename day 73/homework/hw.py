def count(string):
    if string=="":
        return {}
    else:
        dict={}
        for i in string:
            if i not in dict:
                dict[i]=1
            else:
                dict[i]+=1
        return dict



def get_participants(handshakes):
    result=0
    while result*(result-1)/2 < handshakes:
        result+=1
    return result

def high_and_low(numbers):
    numbers = [int(n) for n in numbers.split()]
    return f'{max(numbers)} {min(numbers)}'

def disemvowel(string_):
    result = ""
    vowels = "aeiouAEIOU"
    for letter in string_:
        if letter not in vowels:
            result += letter
    return result

def square_digits(num):
    num = str(num)
    ans = ''
    for i in num:
        ans += str(int(i)**2)
    return int(ans)