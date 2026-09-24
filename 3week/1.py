# def fib(n, cache = {0:0,1:1}):
#     if n in cache:
#         return cache[n]
#     else:
#         cache[n] = fib(n-1,cache) + fib(n-2,cache)
#         return cache[n]

#--------------------------

def fib(N):
    if N <=1:
        return N
    a = 1
    b = 0
    for i in range(N-1):
        a,b = a+b,a
    return a
print(fib(10))