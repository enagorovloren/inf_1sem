import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig = plt.figure(figsize=(10,6))
ax1 = fig.add_subplot(2,3,1)
ax2 = fig.add_subplot(2,3,2)
ax3 = fig.add_subplot(2,3,3)
ax4 = fig.add_subplot(2,3,4)
ax5 = fig.add_subplot(2,3,5)
ax6 = fig.add_subplot(2,3,6)

df = pd.read_csv('iris_data.csv')
v1 = df['SepalLengthCm'].values
v2 = df['SepalWidthCm'].values
v3 = df['PetalLengthCm'].values
v4 = df['PetalWidthCm'].values

ax1.plot(v2,v1,'r.')
ax2.plot(v3,v1,'g.')
ax3.plot(v4,v1,'y.')
ax4.plot(v3,v2,'k.')
ax5.plot(v4,v2,'c.')
ax6.plot(v4,v3,'b.')

ax1.grid()
ax2.grid()
ax3.grid()
ax4.grid()
ax5.grid()
ax6.grid()

plt.show()