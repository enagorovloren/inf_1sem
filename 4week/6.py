import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime


df = pd.read_csv('BTC_data.csv')
date = df['time'].values
close = df['close'].values

pol = np.polyfit(np.arange(0,len(close)),close,3)
print(pol)