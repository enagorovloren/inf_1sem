n = int(input())

def count(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 1

    res = count(n-1)
    if n%2 == 0:
        res = min(res, count(n//2))
    if n%3 == 0:
        res = min(res,count(n//3))

    return res + 1

print(count(n))
    
        
    
    