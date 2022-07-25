import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data=pd.read_csv('data\GDPlist.csv', encoding= 'unicode_escape')#đọc dữ liệu
print(data.head())

data['GDP (millions of US$)'].min() # giá trị nhỏ nhất
data['GDP (millions of US$)'].max() # giá trị lớn nhất

print(data.shape)#số dòng,số cột
print(data.dtypes)#kiểu dữ liệu

data['GDP (millions of US$)'].describe(include = [np.number]) # giá trị lớn nhất

#y/ 5
data_tong = data.pivot_table(values='GDP (millions of US$)', index='Continent',aggfunc ='sum').rename(columns={'GDP (millions of US$)':'tong_GDP'})
data_tb = data.pivot_table(values='GDP (millions of US$)', index='Continent',aggfunc ='mean').rename(columns={'GDP (millions of US$)':'trung_binh_GDP'})
data_gop = data_tong.merge(data_tb,on='Continent',)

print(data['Continent'].mode()) # châu lục xuất hiện nhiều nhất
