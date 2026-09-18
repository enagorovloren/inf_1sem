with open("input4.txt",'r') as file:
    s = file.readline()
    a = list(map(int,s.split()))
    s = file.readline()

fout = open("output4.txt",'w')
if s == '+':
    fout.write(str(sum(a)))
elif s == '-':
    r = 0
    for i in a:
        r -= i
    fout.write(str(r))
else:
    r = 1
    for i in a:
        r *= i
    fout.write(str(r))    
    
    
