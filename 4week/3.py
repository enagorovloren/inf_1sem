import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig = plt.figure(figsize = (10,6))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

df = pd.read_csv('iris_data.csv')
counts = df['Species'].value_counts()

a = counts['Iris-setosa']
b = counts['Iris-versicolor']
c = counts['Iris-virginica']

ax1.pie([a,b,c],autopct='%1.1f%%')


minSize = 1.2
maxSize = 1.5

minCount = 0
midCount = 0
maxCount = 0

for i in df['PetalLengthCm']:
    if i < minSize:
        minCount +=1
    if i >= minSize and i <= maxSize:
        midCount +=1
    if i > maxSize:
        maxCount +=1
ax2.pie([minCount,midCount,maxCount],autopct='%1.1f%%')


plt.show()
