import pickle

import pandas as pd
import statistics
from matplotlib import pyplot as plt

# Esempio di plotting per le statistiche sugli esiti dell'esame di Automatica di Marzo 2022:
values=[]
with open('values.txt') as f:
    lines = f.readlines()
for line in lines:
    values.append(float(line.split("-->     ")[1].replace(',','.').split('\n')[0]))

df=pd.DataFrame({'val':values},index=range(len(values)))

df.plot.kde(bw_method=0.2)
plt.show()
with open('df_001', 'wb') as f:
    pickle.dump(df, f, pickle.HIGHEST_PROTOCOL)
print(statistics.mean(values),statistics.median(values),statistics.variance(values))
print(sorted(values))