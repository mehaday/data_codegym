import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler

df = pd.read_csv("Credit_Scoring.csv")
df.head()
# thông tin dữ liệu
df.info()

# kiểm tra dữ liệu khuyết thiếu
df.isna()

# loại bỏ dữ liệu khuyết thiếu
df1 = df.dropna()

# % số lượng bản ghi còn lại
100 * df1.shape[0]/df.shape[0]

# vẽ biểu đồ phân bố
sns.kdeplot(data=df1["MonthlyIncome"])

# thay thế dữ liệu khuyết thiếu bởi giá trị nội suy theo cột
df2 = df.interpolate(axis=1)

# vẽ biểu đồ box plot cho MonthlyIncome
sns.boxplot(df2["MonthlyIncome"])

# tính giá trị Q1 và Q3
Q1 = df2.quantile(0.25)
Q3 = df2.quantile(0.75)
# tính IQR 
IQR = Q3-Q1
# lọc dữ liệu ngoại lai
df3 = df2[~((df2 < (Q1 - 1.5 * IQR)) | (df2 > (Q3 + 1.5 * IQR))).any(axis=1)]
df3.boxplot()