def capitalize(s):
    a = ''
    b = ''
    for i in range(len(s)):
        if i % 2 == 0:
            a += s[i].upper()
            b += s[i]
        else:
            a += s[i]
            b += s[i].upper()
    return [a, b]
def solution(nums):
    if nums is None:
        return []
    return sorted(nums)



def nth_even(n):
    return 2 * (n-1)
def smaller(arr):
    result = []
    for i in range(len(arr)):
        count = 0
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                count += 1
        result.append(count)
    return result
def reverse_number(n):
    if n < 0:
        positive_n = -n          
        reversed_str = str(positive_n)[::-1]   
        return -int(reversed_str)   
    else:
        reversed_str = str(n)[::-1]
        return int(reversed_str)
    