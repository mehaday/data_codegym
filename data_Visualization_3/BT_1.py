import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# [Bài tập] Vẽ biểu đồ kết hợp – House Price Đống Đa

df=pd.read_excel('\data\house_price_dống-da.xlsx')
df.head()


# lọc khuyết thuyết

df=df.dropna()

df.head()


# Vẽ biểu đồ xu hướng phân tích mối quan hệ giữa giá nhà với diện tích, giá nhà với số lượng phòng ngủ, nhận xét.

#fig, (ax1, ax2) = plt.subplots(1,2, figsize=(10,4), sharey=True, dpi=120)
sns.lmplot(data=df,x='price',y='area')
#plt.subplot(1,2,2)
sns.lmplot(data=df,x='price',y='bedroom')


# Vẽ biểu đồ phân bố thể hiện phân bố của giá nhà theo các hướng, nhận xét.

sns.violinplot(data=df,x='price',y='house_direction')


# Vẽ biểu đồ tần số để đếm số nhà ở mỗi hướng nhà, nhận xét.

sns.countplot(data=df,x='house_direction')


# Vẽ biểu đồ boxplot thể hiện phân bố của giá nhà theo các hướng, nhận xét.
# 

sns.boxplot(data=df,x='house_direction',y='price')