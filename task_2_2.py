n = int(input())
str = input()
l = [str[i:i+n] for i in range(0,len(str),n)]
s = [x[::-1] for x in l]
str = ""
for i in s:
    str +=i
print(str)