import numpy as np

N,M = map(int,input().split())
A = np.zeros(N * M)
A = A.reshape(N,M)

for i in range(N):
    A[i,0:M] = list(map(int,input().split()))


def det(m):
    r,c = m.shape
    if r == c and r == 2:
        return m[0,0] * m[1,1] - m[0,1] * m[1,0]
    else:
        d = 0
        for i in range(c):
            d += ((-1)**i) * (det(np.delete(np.delete(m,0,axis=0),i,axis=1))) * m[0,i]
        return d
A0 = np.copy(A)
DET = det(np.delete(A,M-1,axis=1))
if DET == 0:
    print("Решений нет или их бесконечно много")
else:
    for i in range(N):
        A = np.copy(A0)
        A[:,i] = A0[:,M-1]
        A = A[:, :-1]
        print(det(A)/DET)