import numpy as np

n,m = map(int,input().split())

u = 0
d = n-1
l = 0
r = m-1
N = 0
a = np.zeros((n,m))

while u <= d and l <= r:
    a[u,l:r+1] = np.arange(N,N + r-l + 1) + 1
    N += r-l+1
    u += 1

    a[u:d + 1,r] = np.arange(N,N + d - u + 1) + 1
    N += d-u+1
    r -= 1

    a[d,l:r+1] = np.arange(N+r-l,N-1,-1) + 1
    N += r - l + 1
    d -= 1

    a[u:d+1,l] = np.arange(N + d - u,N-1,-1)+1
    N += d - u + 1
    l += 1
print(a)

