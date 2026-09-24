N = int(input())
a = list(map(int, input().split()))

for i in a:
    m = 0
    for j in a:
        if j < i:
            m += 1
    if m == N // 2:
        print(i)
        break