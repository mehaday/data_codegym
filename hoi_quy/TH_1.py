import pandas as pd # Khai báo thư viện hỗ trợ đọc và phân tích dữ liệu ở dạng bảng
dataset = pd.read_csv("salary_data.csv") # Lấy dữ liệu từ file work_data.csv đê phân tích và đặt tên dữ liệu đó là dataset
dataset.tail(10) # xem 5 dòng đầu tiên của bảng dữ liệu

dataset.shape # số lượng quan sát

dataset.describe()

import matplotlib.pyplot as plt  # Khai báo thư viện để vẽ hình
dataset.plot(x='SoNamKinhNghiem', y='Luong', style='o')  
plt.title('số năm kinh nghiệm - lương')  
plt.xlabel('số năm kinh nghiệm')  
plt.ylabel('lương')  
plt.show()

# vẽ biểu đồ histogram
plt.hist(dataset['Luong'],20)
plt.show()

df_keToan = dataset[dataset["NganhNghe"] == "KeToan"]
df_hcnh = dataset[dataset["NganhNghe"] == "HCNS"]
df_sale = dataset[dataset["NganhNghe"] == "Sale"]

print ("Kết cấu bộ dữ liệu")
print ("Số lượng mẫu nhân viên kế toán: " + str(df_keToan.shape[0]))
print ("Số lượng mẫu nhân viên HCNH: " + str(df_hcnh.shape[0]))
print ("Số lượng mẫu nhân viên SALE: " + str(df_sale.shape[0]))

n_by_nganhNghe = dataset.groupby("NganhNghe")["Luong"].mean()
n_by_nganhNghe

# Biểu đồ phân bố lương của nhân viên Kế toán
plt.boxplot(df_keToan['Luong'])
plt.show()