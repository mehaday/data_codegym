import pandas as pd
import matplotlib.pyplot as plt

d = pd.read_csv("data/FoodPrice_in_Turkey.csv")

d11 = d[(d['Year'] == 2019) & (d['Month'] == 12) & (d['ProductName'] == 'Milk (powder, infant formula) - Retail')].reset_index()
d12 = d[(d['Year'] == 2019) & (d['Month'] == 12) & (d['ProductName'] == 'Fuel (gas) - Retail')].reset_index()
data1 = pd.DataFrame({'x': d11['Place'], 'y1': d11['Price'], 'y2': d12['Price']})

data1.plot(x = 'x', y = ['y1', 'y2'], kind = 'bar')
plt.title('Milk and Gas Price in 12/2019', fontsize = 16, color = 'r')
plt.xlabel('Place', fontsize = 14)
plt.ylabel('Price', fontsize = 14)
plt.show()