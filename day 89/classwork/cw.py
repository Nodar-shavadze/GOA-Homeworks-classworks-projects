def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
#3
def kebabize(s):
    result = ""
    
    for c in s:
        if c.isdigit():
            continue  
        
        if c.isupper():
            
            if result:
                result += "-"
            result += c.lower()
        else:
            result += c
#4
def is_isogram(s):
    cleaned = s.lower()
    return len(set(cleaned)) == len(cleaned)
#5
