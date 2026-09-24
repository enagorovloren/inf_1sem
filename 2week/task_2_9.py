s = input()
count = 0
flag = False
for i in s:
    if (i == '.' or i=='!' or i=='?') and not flag:
        count += 1
        flag = True
    elif (i != '.' and i!='!' and i!='?') and flag == True:
        flag = False

print(count)