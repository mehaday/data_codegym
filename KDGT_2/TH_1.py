# Khai báo thư viện
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

# đọc dữ liệu
df = pd.read_csv("FoodPrice_in_Turkey.csv")
# lọc dữ liệu gạo bán lẻ (Rice - Retail) ở National Average
df_rice = df[(df.ProductName == "Rice - Retail") & ( df.Place == "National Average")]
print("kích thước bộ dữ liệu: " ,df_rice.shape)
print ("mô tả bộ dữ liệu")
df_rice.describe()

# vẽ mối hiên hệ giữa thời gian và giá gạo
df_rice['time'] =  pd.to_datetime(df_rice['Year'].astype(str) + '/'+df_rice['Month'].astype(str))
plt.plot(df_rice['time'], df_rice['Price'], linewidth = 2, marker = '*', markersize=2, markerfacecolor='red', markeredgecolor = 'blue', markeredgewidth=2)
plt.show()

# Biến đổi thời gian
df_rice['time_processed'] = df_rice.Month + (df_rice.Year -2013)*12
# Vẽ lại biểu đồ liên hệ giữa time_processed và giá gạo
plt.plot(df_rice['time_processed'], df_rice['Price'], linewidth = 2, marker = '*', markersize=2, markerfacecolor='red', markeredgecolor = 'blue', markeredgewidth=2)
plt.show()