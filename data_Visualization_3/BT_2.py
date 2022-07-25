import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# [Bài tập] Vẽ biểu đồ kết hợp – Shopee.ph Korean-top clothing

dt = pd.read_csv('data/shopeep_koreantop_clothing_shop_data.csv')
dt.head()

dt=dt.dropna()


# Vẽ biểu đồ tần số số lượng shop gia nhập theo các năm.

sns.countplot(data=dt,x='join_year')


# Vẽ biểu đồ xu hướng thể hiện mối quan hệ giữa tỉ lệ phản hồi với số lượt khách hàng đánh giá tốt.

sns.lmplot(data=dt,x='rating_good',y='response_rate')


# Vẽ biểu đồ xu hướng thể hiện mối quan hệ giữa thời gian phản hồi (đơn vị giây) với số lượt khách hàng đánh giá xấu.


dt['response_time']=pd.to_datetime(dt.response_time,format=' %H:%M:%S')
#dt['response_time']=dt['response_time'].dt.seconds.astype(int)

import time
dt['seconds'] = [time.mktime(t.timetuple()) for t in dt.response_time]

sns.lmplot(data=dt,x='seconds',y='rating_bad')


# Vẽ biểu đồ thể hiện phân bố của điểm đánh giá trung bình. 

sns.violinplot(data=dt,x='rating_normal')


# Vẽ biểu đồ tần số của cửa hàng chính thức và không chính thức.

sns.countplot(data=dt,x='is_official_shop')


# Vẽ biểu đồ tần số của cửa hàng được xác thực với chưa xác thực. 

sns.countplot(data=dt,x='is_shopee_verified')
