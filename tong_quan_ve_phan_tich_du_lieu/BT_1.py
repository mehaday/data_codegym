import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('data\GDPlist.csv', encoding= 'unicode_escape')

data.info()

plt.hist(data, bins = 200)
plt.show()

data.groupby('Continent')

data = data.sort_values('Continent',ascending = False)