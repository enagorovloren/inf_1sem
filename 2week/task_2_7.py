a = list(map(int,input().split()))
m = 0
index = 0
for i in range(0,len(a)):
    cur = 0
    for j in range(0,len(a)):
        if a[i] == a[j]:
            cur += 1
    if cur > m:
        m = cur
        index = i
print(a[index])