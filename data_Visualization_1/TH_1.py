import pandas as pd
import matplotlib.pyplot as plt

d = pd.read_csv("data/FoodPrice_in_Turkey.csv")

data1 = d[(d['Year'] == 2019) & (d['Month'] == 12) & (d['ProductName'] == 'Rice - Retail')]

plt.bar(data1['Place'], data1['Price'])
plt.show()

plt.bar(data1['Place'], data1['Price'], width = 0.5)
plt.title('Rice Price in 12/2019', fontsize = 16, color = 'r')
plt.xlabel('Place', fontsize = 14)
plt.ylabel('Price', fontsize = 14)
plt.show()

data2 = d[(d['Place'] == 'National Average') & (d['Year'] == 2019) & (d['ProductName'] == 'Rice - Retail')]

plt.plot(data2['Month'], data2['Price'])
plt.show()