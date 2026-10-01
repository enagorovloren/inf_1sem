size,symb = input().split()
size = int(size)

j = size
for i in range(1,size+1):
    print(symb * min(i,j))
    j -= 1

