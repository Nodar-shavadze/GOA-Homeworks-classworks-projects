 #1
def no_boring_zeros(n):
    if n == 0:
        return 0

    while n % 10 == 0:
        n = n // 10

    return n
#2
def to_binary(n):  
    output=[]
    while n>=1:
        b = n % 2
        n = n // 2
        output.append(str(b))
    output.reverse()
    out=''.join(output)
    return int(out)
#6
def what_century(year):
    g=  (int(year) + 99) // 100
    f=str(g)
    if f[0]== "1":
        return f"{f}th"
    if f[1] == "1" :
        return f"{f}st"
    if f[1] == "2":
        return f"{f}nd"
    if f[1] == "3" :
        return f"{f}rd"        
    return f"{f}th"
#5