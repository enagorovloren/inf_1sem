s = input()

vowelDict = ['а','о','у','и','е','я','ю','ё','ы','э']
consonants = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ','ъ','ь']
r=""
for i, char in enumerate(s):
    if i == 0 and char in vowelDict and len(s) == 1:
         r += char+'с'+char
    elif i == 0 and char in vowelDict and s[1] not in vowelDict:
        r += char+'с'+char
    elif i != 0 and char in vowelDict and s[i - 1] in consonants:
        r += char +'с'+char
    else:
        r += char
print(r)