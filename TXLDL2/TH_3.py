import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, OrdinalEncoder

# đọc dữ liệu
df = pd.read_csv("OnlineRetail.csv", encoding = "ISO-8859-1")

# in ra kich thuoc du lieu
df.shape

df.head()
df.info()

# kiểm tra dữ liệu bị khuyết
df.isna()
# kiểm tra dữ liệu không bị khuyết
df['CustomerID'].notna()

# in những dòng ngoại lai Quantity < 0
df[df['Quantity'] < 0]

#Xóa bỏ dòng ngoại lai của Quantity
df = df[df['Quantity'] >= 0]

# xóa những dòng chứa toàn giá trị khuyết
df2 = df.dropna(how='all')

# giữ những dòng có ít nhất 7 giá trị không bị khuyết
df3 = df.dropna(thresh=7)

# xóa những hàng mà có giá trị bị khuyết trên cột CustomerID
df4 = df.dropna(subset=["CustomerID"])
df4.shape
# thay thế những giá trị bị khuyết trên cột CustomerID bằng giá trị -1
df5 = df
df5['CustomerID'] = df['CustomerID'].fillna(-1)
# hiển thị những dòng có CustomerID = -1 vừa được thay thế
df5[df5['CustomerID'] == -1]

# thay thế các giá trị bị khuyết ở cột Country bằng giá trị trước nó
df5['Country'] = df['Country'].fillna(method='ffill')

