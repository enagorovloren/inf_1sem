str = input()
n = len(str)

mirror_sym = ['A', 'H', 'I', 'M', 'O', 'T', 'U','V', 'W', 'X', 'Y', '1', '8']
el = {'E':'3','J':'L','S':'2','Z':'5'}

def isPalindrome(str):
    for i in range(0, int(n/2) + 1):
        if (str[i] != str[n-1-i]):
            return False
    return True

def isMirror(str):
    for i in range(0, int(n/2)+1):
        if (str[i] == str[n-1-i] and str[i] in mirror_sym):
            continue
        elif(((str[i],str[n-1-i]) in el.items()) or ((str[n-1-i],str[i]) in el.items())):
            continue
        elif (str[i] != str[n-1-i] or str[i] not in mirror_sym):
            return False
    return True
        
a = isPalindrome(str)
b = isMirror(str)

if a and b:
    print(f"{str} is mirrored palidrome")
elif a and not b:
    print(f"{str} is classic palindrome")
elif not a and b:
    print(f"{str} is classic mirror")
else:
    print(f"{str} is boring string(")