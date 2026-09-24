size,symb = input().split()
size = int(size)

for i in range(1,size+1):
    if size % 2 != 0:
        print(symb * (round(size/2) - abs(round(size / 2) - i)))
    else: print("c\ncc\nccc\nccc\ncc\nc")