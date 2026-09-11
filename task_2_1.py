n = int(input())
l = list(map(int, input().split()))
arr = [i for i in range(1,n+1)]

for i in l:
    arr.remove(i)

print(arr)