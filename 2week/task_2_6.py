a = list(map(int,input().split()))
for i in range(0,len(a)):
    b = True
    for j in range(0,len(a)):
        if a[i] == a[j] and i != j:
            b = False
    if b:
        print(a[i])