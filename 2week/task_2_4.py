s = input().split()
s[0:-1:2], s[1::2]=s[1::2], s[0:-1:2]
print(*s)
