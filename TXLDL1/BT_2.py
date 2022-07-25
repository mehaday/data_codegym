import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler


df = pd.read_excel('\data\house_price_dống-da.xlsx')


# Xóa dữ liệu khuyết thiếu khi thuộc tính price không có giá trị
df.dropna(subset=['price'], inplace=True)

lis_row = ['house_direction', 'balcony_direction', 'toilet', 'bedroom', 'floor']
lis_mode = []
for i in lis_row:
    lis = list(df[i].mode())
    lis_mode.append(lis)



values = {}
for i in range(len(lis_row)):
    value = {lis_row[i]: lis_mode[i][0]}
    values.update(value)

df = df.fillna(value=values)
df = df[(df['type_of_land'] == "Bán nhà riêng")]

# Tính 1 mthì bao nhiêu tiền
df['price/m2'] = df['price'] / df['area']

Q1 = df['price/m2'].quantile(0.25)
Q3 = df['price/m2'].quantile(0.75)
IQR = Q3 - Q1
df2 = df[~((df["price/m2"] < Q1-1.5*IQR) | (df["price/m2"] > Q3+1.5*IQR))]

# Chuẩn hóa dữ liệu
# min-max scaling
scaler = MinMaxScaler()
mms = scaler.fit_transform(pd.DataFrame(df2['price/m2']))

# Robust scaling
scaler = RobustScaler()
rbs = scaler.fit_transform(pd.DataFrame(df2['price/m2']))

# Z-score scaling
scaler = StandardScaler()
zss = scaler.fit_transform(pd.DataFrame(df2['price/m2']))

# Dữ liệu gốc
sns.kdeplot(data=df['price/m2'])
plt.show()

# Dữ liệu đã thay đổi
sns.kdeplot(data=mms)
plt.show()

sns.kdeplot(data=rbs)
plt.show()

sns.kdeplot(data=zss)
plt.show()