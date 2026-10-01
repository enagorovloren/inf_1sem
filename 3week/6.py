x = list(map(float,input().split()))
y = list(map(float,input().split()))

z = [x[i] * y[i] for i in range(0,len(x))]
x2 = [i ** 2 for i in x]

b = (len(z) * sum(z) - sum(x) * sum(y)) / (len(x) * sum(x2) - (sum(x))**2)
a = (sum(y) - b * sum(x))/len(x)

print(f"{b}x + {a}")