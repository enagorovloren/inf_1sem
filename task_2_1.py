n = int(input())
l = list(map(int, input().split()))
arr = []
for i in range(1,n+1):
    arr.append(i)

for i in l:
    arr.remove(i)

print(arr)