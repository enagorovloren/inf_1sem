import numpy as np

n,m = map(int,input().split())

ur = 0
dr = n-1
lc = 0
rc = m-1

a = np.zeros((n,m))

val = 0
while(rc != lc and ur != dr):
    for i in range(lc,rc+1):
        a[ur,i] = val
        val+=1
    ur -=1
    for i in range(ur,dr+1):
        a[i,rc] = val
        val+=1
    rc -= 1
    for i in range(rc,lc-1,-1):
            a[dr,i] = val
            val+=1
    dr +=1
    for i in range(dr,ur-1,-1):
            a[i,lc] = val
            val+=1
    lc +=1
print(a)
