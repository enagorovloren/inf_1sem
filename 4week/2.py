import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig = plt.figure(figsize = (10,6))
ax1 = fig.add_subplot(311) 
ax2 = fig.add_subplot(312)
ax3 = fig.add_subplot(313) 


v1 = np.random.normal(0, 10, 1000)
 
ax1.hist(v1, 50)
ax1.grid() 


v2 = np.random.normal(0,10,100000)

ax2.hist(v2,50)
ax2.grid()

v3 = np.random.normal(0,10,10000000)
ax3.hist(v3,50)
ax3.grid()

plt.show()
