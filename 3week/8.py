import random
import numpy as np

def gen(N, a, b, sigma, x_min, x_max):
    X = []
    Y = []
    for _ in range(N):
        x = random.uniform(x_min, x_max)
        X.append(x)
        noise = random.gauss(0, sigma)
        y = a * x + b + noise
        Y.append(y)    
    return X, Y

Np = 1000
a0 = 2.5
b0 = 5.0

X, Y = gen(Np, a0, b0, 1.5,0,10)

a1, b1 = np.polyfit(X, Y, 1)

print(f"{b0}x + {a0}")
print(f"{b1}x + {a1}")