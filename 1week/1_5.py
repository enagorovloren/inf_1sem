with open('input5.txt','r') as fin:
    s = fin.readline()
N,b,c = map(int,s.split())

val = 0
N = str(N)
for i in range(len(N)):
    val += int(N[-i-1])*b**i

res=''
while(val > 0):
    res += str(val%c)
    val = val // c

with open('output5.txt','w') as fout:
    fout.write(res[::-1])