import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig = plt.figure(figsize=(10,6))

y1 = np.array([127.10,256.56,384.01,516.76,637.66,778.60,905.70,1042.30,1171.00])
y2 = np.array([103.00,208.70,313.10,419.40,524.80,632.90,740.80,849.00,961.40])
y3 = np.array([220.45,441.70,622.77,884.10,1106.25,1328.80,1550.57,1774.21,1996.61])
y4 = np.array([187.60,375.31,563.83,751.59,941.40,1128.70,1320.60,1510.20])
y5 = np.array([165.22,331.54,497.86,664.18,830.60,998.56,1166.54,1335.97])



plt.plot(np.arange(1,10),y1,'bo-')
plt.plot(np.arange(1,10),y2,'ro-')
plt.plot(np.arange(1,10),y3,'ko--')
plt.plot(np.arange(1,9),y4,'g^-')
plt.plot(np.arange(1,9),y5,'yo-')

plt.show()
            