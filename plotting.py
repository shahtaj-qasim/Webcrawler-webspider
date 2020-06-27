import matplotlib.pyplot as plt

import pandas as pd

# plotting
cols_to_use = ['hasGA', 'hasIPAnon']
df= pd.read_csv('C:/Users/lenovo/PycharmProjects/gadetector/garesults.csv', usecols= cols_to_use)


df1 = df.apply(pd.value_counts)
print (df1)
df1.plot.bar()
plt.show()

