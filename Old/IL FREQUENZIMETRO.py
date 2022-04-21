import pandas as pd
from matplotlib import pyplot as plt

string = "audhbferuybdihbueryihburyihfbwuyfbuyvbeoifybfeyvuucshdifyuwgdhwgggacgvvvhag" \
         "teujcbxbxjdccyhfjujirurjfhyfhyrhejdieokeidhdiwppwiddkj"

frequency = {}
for letter in set(string):
    frequency[letter] = string.count(letter)
frequency = dict(sorted(frequency.items(), key=lambda item: -item[1]))
print(frequency)
df = pd.DataFrame({"values": frequency.values()}, index=frequency.keys())
df.plot.pie(y="values")
plt.show()
