import pandas as pd
from scipy import  stats
import matplotlib.pyplot as plt

df = pd.read_excel("data\Coca_cola_use.xlsx", index_col= 'STT')
print ("5 bản ghi đầu tiên của bộ dữ liệu ")
print (df.head())

print ("thông tin bộ dữ liệu")
print (df.info())

print ("mô tả bộ dữ liệu")
print (df.describe())

df.boxplot()

print (stats.ttest_ind(df.Ohio, df.Atlanta,equal_var=False))