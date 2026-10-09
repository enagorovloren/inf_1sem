import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime


df = pd.read_csv('BTC_data.csv')
date = df['time'].values
close = df['close'].values
newTime = []

def newDate(date_string):
    dt_obj = datetime.strptime(date_string, '%Y-%m-%d')
    # Форматируем объект в нужную строку
    new_date_string = dt_obj.strftime('%d-%m-%Y')
    return new_date_string

for i in range(0,len(date)):
    a = date[i].find('T')
    s = date[i][0:a]
    newTime.append(newDate(s))


plt.plot(newTime,close,'k--')
plt.grid()
plt.show()