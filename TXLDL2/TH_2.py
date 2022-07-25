import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, OrdinalEncoder

# đọc dữ liệu
df = pd.read_csv("FoodPrice_in_Turkey.csv", encoding = "ISO-8859-1")

# in ra kich thuoc du lieu
df.shape

# mô tả dữ liệu
df.describe()

# thông tin dữ liệu
df.info()

# kiểm tra dữ liệu bị khuyết
df.isna()

# kiểm tra dữ liệu không bị khuyết
df.notna()

# xóa những dòng chứa giá trị bị khuyết
df1 = df.dropna()

sns.boxplot(x=df1['Price'])  # vẽ box plot cho dữ liệu ở cột Price

Q1 = df1['Price'].quantile(0.25)
Q3 = df1['Price'].quantile(0.75)
IQR = Q3 - Q1

# xác định phần tử không phải ngoại lai
df2 = df1
df2['outlier'] = ~((df1['Price'] < (Q1 - 1.5*IQR)) | (df1['Price'] > (Q3 + 1.5*IQR)))

# xóa phần tử ngoại lai
df2 = df2[df2['outlier'] == True]

sns.boxplot(x=df2['Price'])  # vẽ box plot cho dữ liệu ở cột Price