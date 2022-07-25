# [Bài tập] Kiểm định House Price Đống Đa Hà Nội

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.preprocessing import StandardScaler
import scipy

data = pd.read_csv('data\house_price_Dống-Da_Hà-Nội_subdata.csv')
data.head()

data = data.loc[:,['price','land_certificate','property_type']]
data

data['land_certificate'].unique()

condition = (data.price.isna() | data.property_type.isna() )#| data.land_certificate.isna() )

data = data[condition==False]

data.info()

tg = data['price'].dropna()

# Vẽ biểu đồ so sánh phân phối giá (triệu đ/m2) giữa nhà Phố và Nhà ngõ

data1 = data.loc[data['property_type']=='trong ngo']
data1

data2 = data.loc[data['property_type']=='mat pho']
data2

sns.kdeplot(data=data1)


plt.boxplot(data1['price'])

data1 = data1.loc[data1['price'] <= 17000]
data1

sns.kdeplot(data=data1)

plt.boxplot(data1['price'])

sns.kdeplot(data=data2)


plt.boxplot(data2['price'])

data2 = data2.loc[data2['price'] <= 50000]
data2

sns.kdeplot(data=data2)

# Kiểm định giả thuyết giá (triệu đ/m2) nhà mặt phố cao hơn giá nhà trong ngõ với mức ý nghĩa 5%
# kiểm định phía phải

data1 = data1['price']
data1

data2 = data2['price']
data2

data2.isnull().any()

t_statistic3 , p_value3 = scipy.stats.ttest_ind(data1[data1['property_type']=='trong ngo']['price'],data2[data2['property_type']=='mat pho']['price'],equal_var=False)
t_statistic3,p_value3

2*0.05 > p_value3

# do t_statistic < 0 , nên không đủ điều kiện bác bỏ H0, chính vì vậy cx ko đủ điều kiện chấp nhận H1

# Giá của những căn nhà không có thông tin về giấy tờ pháp lý thấp hơn giá nhà những căn có thông tin về giấy tờ pháp lý với mức ý nghĩa 5%

t_statistic4 , p_value4 = scipy.stats.ttest_ind(data1[data1['land_certificate']=='So do']['price'],data2[data2['land_certificate']=='NaN']['price'])
t_statistic4,p_value4
