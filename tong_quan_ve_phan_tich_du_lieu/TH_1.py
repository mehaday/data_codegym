import pandas as pd
import matplotlib.pyplot as plt
# Đọc bộ dữ liệu
data=pd.read_csv('data\subset-covid-data.csv', encoding= 'UTF-8')

data.head()

# Số lượng dòng và cột của bộ dữ liệu
data.info()

# Tìm hiểu xem dữ liệu được thống kê cho những ngày nào
data.date.value_counts()

# lọc dữ liệu nhiễu:
cleaned_data = data[data.date == '2020-04-12']

# Vẽ biểu đồ phân bố số lượng ca mắc mới ở các quốc gia
print ("trung bình số ca mắc mới: " + str(cleaned_data.cases.mean()))
print ("trung vị của số ca mắc mới: "+ str(cleaned_data.cases.median()))

plt.hist(cleaned_data.cases, bins = 200)
plt.title("Phân bố số ca mắc mới")
plt.xlabel("số số ca mắc mới")
plt.ylabel("Số lượng quốc gia")

plt.show()

# Tổng số ca mắc mới, số ca tử vong ở từng châu lục
cleaned_data.groupby('continent')['cases','deaths'].sum()

# 5 quốc gia có số ca nhiễm mới cao nhất
data = data.sort_values('cases',ascending = False)
data.head(5)


#  Top 5 quốc gia có số ca tử vong cao nhất
data = data.sort_values('deaths',ascending = False)
data.head(5)