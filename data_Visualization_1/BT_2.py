# [Bài tập] Phân tích bộ dữ liệu HousePrice _ Đống Đa
import pandas as pd
import matplotlib.pyplot as plt
import seaborn

data=pd.read_excel('data\house_price_dống-da.xlsx')
data.head()


# Vẽ biểu đồ phân tích mối liên hệ giữa diện tích với giá nhà, giữa số phòng ngủ với giá nhà, giữa số toilet với giá nhà.


data1=data[['area','bedroom','toilet','price']]
data1


data2=data1[data1.bedroom.isna()==False]
data2


data3=data2[data2.toilet.isna()==False]


data4=data3[data3.price.isna()==False]
data4


from matplotlib.pyplot import figure
figure(figsize=(8, 6), dpi=80)
plt.hist(data4['price'])
plt.show()


#  Vẽ biểu đồ thể hiện tỉ lệ % bài đăng (bản ghi) giữa các hình thức nhà (type_of_land).

data_type_of_land = data['type_of_land'].value_counts()
data_type_of_land


ck=pd.DataFrame(data_type_of_land)


from matplotlib.pyplot import figure
figure(figsize=(16, 9), dpi=80)
myexplode = [0.2, 0, 0, 0, 0, 0, 0, 0, 0]
plt.pie(ck)
plt.legend(title='Tỉ lệ bản ghi giữa các hình thức bán nhà( Type_of_land) :')
plt.show()





# # Vẽ biểu đồ so sánh giá nhà trung bình trên 1 m2 giữa các hình thức nhà (type_of_land)


dt = data[['type_of_land','price']]
dt


dt=dt[dt.price.isna()==False]
dt


dt=dt[dt.type_of_land.isna()==False]
dt


dt1 = dt.groupby(['type_of_land'])['price'].mean().reset_index(name='mean_price')
dt1


plt.pie(dt1['mean_price'],labels=dt1['type_of_land'])


# # Vẽ biểu đồ thể hiện sự thay đổi giá nhà trung bình trên 1m2 theo số lượng phòng ngủ.


test=data[['bedroom','price']]
test


test1=test[test.bedroom.isna()==False]


test1=test1[test1.price.isna()==False]


check= test1.groupby(['bedroom'])['price'].mean().reset_index(name='mean_for_bedroom')
check


plt.bar(check['bedroom'],check['mean_for_bedroom'])
