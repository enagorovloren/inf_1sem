import string
import heapq

def punct(text):
    translator = str.maketrans(string.punctuation,' ' * len(string.punctuation))
    return text.translate(translator)

with open('PYTHON-LICENSE.txt','r') as fin:
    with open('out.txt','w') as fout:
        for i in fin:
            fout.write(punct(i).lower())

words = {}
with open('out.txt','r') as fin:
    for s in fin:
        for w in s.split():
            if w not in words:
                words[w] = 1
            else:
                words[w] +=1

print(heapq.nlargest(5,words.keys(),key=words.get))