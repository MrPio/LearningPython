import pickle

import pandas as pd
from matplotlib import pyplot as plt

# Esempio di plotting per le statistiche sull'età:

df = pd.DataFrame({'val': [10, 20, 30, 40, 50, 60, 70, 80, 90], 'sex': list("MFMFFFMMM")},
                  index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'])
df.plot.pie(y="val")
df.hist(column=["val"], by="sex")
df.plot.line(column=["val"], by="sex")
plt.show()
with open('df_001', 'wb') as f:
    pickle.dump(df, f, pickle.HIGHEST_PROTOCOL)
