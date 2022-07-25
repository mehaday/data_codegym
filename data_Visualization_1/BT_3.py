# Bài tập Phân tích bộ dữ liệu Shopee.ph**
import pandas as pd
import matplotlib.pyplot as plt
import seaborn

dataframe = pd.read_csv('data/shopeep_koreantop_clothing_shop_data.csv')
dataframe.head()


dataframe.info()

# Vẽ biểu đồ so sánh số lượng shop gia nhập theo các năm.

dk=dataframe[['name','join_year']]
dk


dk=dk.groupby('join_year')['name'].count().reset_index(name='amount join')
dk


plt.bar(dk['join_year'],dk['amount join'])
plt.legend(title='số lượng shop gia nhập theo các năm')
plt.show()

# Vẽ biểu đồ thể hiện mối quan hệ giữa tỉ lệ phản hồi với số lượt khách hàng đánh giá tốt.


dk1=dataframe[['response_rate','rating_good']]
dk1


dk1=dk1[dk1.rating_good.isna()==False]
dk1


plt.scatter(dk1['response_rate'],dk1['rating_good'])

# Vẽ biểu đồ thể hiện mối quan hệ giữa thời gian phản hồi (đơn vị giây) với số lượt khách hàng đánh giá xấu.


dk2=dataframe[['response_time','rating_bad']]
dk2



from datetime import datetime
pt = datetime.strptime(dk2['response_time'].loc[1],'%H:%M:%S')
total_seconds = pt.second + pt.minute*60 + pt.hour*3600

# Vẽ biểu đồ thể hiện xu hướng của số lượng shop gia nhập theo thời gian.


d=dataframe[['name','join_year','join_month','join_day']]
d


d1=d.groupby('join_year')['name'].count().reset_index(name='amount join')
d1


d2=d.groupby('join_month')['name'].count().reset_index(name='amount join')
#d1=d1.sort_index('join_month')
d2


d3=d.groupby('join_day')['name'].count().reset_index(name='amount join')
#d1=d1.sort_index('join_month')
d3


from matplotlib.pyplot import figure
figure(figsize=(16, 9), dpi=80)
plt.subplot(1,3,1)
plt.bar(d1['join_year'],d1['amount join'])

plt.subplot(1,3,2)
plt.xticks(rotation=45)
plt.bar(d2['join_month'],d2['amount join'])

plt.subplot(1,3,3)
plt.plot(d3['join_day'],d3['amount join'])


plt.show()

# Vẽ biểu đồ thể hiện phân bố của điểm đánh giá trung bình.

k=dataframe[['rating_star']]


plt.hist(k)
plt.show()


import seaborn as sns
sns.kdeplot(data=k)
