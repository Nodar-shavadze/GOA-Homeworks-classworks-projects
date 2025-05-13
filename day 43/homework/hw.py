def remove_char(s):
    return s[1:-1]

def build_string(*args):
    return f'I like {" and ".join(args)}.'

def contamination(text, char):
    return char * len(text)

def is_palindrome(s):
    return s == s[::-1]

def obfuscate(email):
    return email[0] + '*****' + email[email.index('@'):]

print(remove_char("abcdef"))
print(build_string("football", "basketball", "baseball"))
print(contamination("abc", "z"))
print(is_palindrome("madam"))
print(obfuscate("example@example.com"))

string_example = "  Hello, World!  "
print(string_example.strip())
print(string_example.lower())
print(string_example.upper())
print(string_example.replace("World", "Python"))
print(string_example.split(','))

list_example = [1, 2, 3, 4, 5]
list_example.append(6)
print(list_example)

list_example.remove(2)
print(list_example)

list_example.reverse()
print(list_example)

list_example.sort()
print(list_example)
