with open('input6.txt','r') as fin:
    s = fin.readlines()
arr = [int(x) for x in s[0].split()]
op = s[1].strip()
base = int(s[2])

l = []

for N in arr:
    val = 0
    N = str(N)
    for i in range(len(N)):
        val += int(N[-i-1])*base**i
    l.append(val)


out = 0
if op == '+':
    out = sum(l)
elif op =='-':
    for i in l:
        out -= i
else:
    out = 1
    for i in l:
        out *= i

res=''
while(out > 0):
    res += str(out%base)
    out = out // base
print(res[::-1])

with open('output6.txt','w') as fout:
    fout.write(res[::-1])