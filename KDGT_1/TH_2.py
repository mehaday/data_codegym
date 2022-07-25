import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_excel('data\Quality.xlsx')
print(df.head())
df.info()

# Tiền xử lý dữ liệu
# gom hết dữ liệu của 4 mẫu thành 1 mảng duy nhất
sample = list()
for i in df.columns:
    sample.extend(df[i].tolist())

# tiến hành mô tả dữ liệu mẫu
df = pd.DataFrame(columns=['sample'], data= sample) 
df.describe()