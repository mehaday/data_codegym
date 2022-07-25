import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.preprocessing import StandardScaler
import scipy

df = pd.read_csv('data/GDPlist.csv',encoding='ISO-8859-1')
df.head()

# Lọc dữ liệu

df.isnull().any()

df.dtypes

sns.kdeplot(data=df)

df = df['GDP (millions of US$)']
df

df['Continent'].unique()

df['GDP'] = df['GDP (millions of US$)']
df

tg = df.loc[df.GDP >= 500000]
tg

df.boxplot()

# Kiểm định giả thuyết

# Trung bình GDP của các quốc gia trên thế giới là 500 tỉ usd/năm

# H0 : mean(GDP) = 500 tỉ <br>
# H1 : ≠ 500 tỉ
# 
# => là kiểm định 2 phía

t_statistic,p_value = scipy.stats.ttest_1samp(df,500000)
t_statistic,p_value

# Giả sử chọn mức ý nghĩa alpha = 5% = 0.05
#  
# ta thấy p_value > alpha nên loại H0 không thành công,  không đủ cơ sở chấp nhận  H1
# 
# => Trung bình GDP của các quốc gia trên thế giới là 500 tỉ usd/năm là đúng

# GDP trung bình ở các quốc gia ở châu Âu cao hơn châu Á không

# H0:1- 2<=0 ( GDP(châu á) -châu âu <0)
# 
# H1:1- 2>0 ( GDP( á) - âu >0 ) 
# 
# => kiểm định phía phải

df1 = df.loc[df['Continent']=='Asia']
df1

df1 = df1['GDP']

df2 = df.loc[df['Continent']=='Europe']
df2 = df2['GDP']
df2

t_statistic1 , p_value1 = scipy.stats.ttest_ind(df1,df2,equal_var=False)
t_statistic1,p_value1


df3 = df.loc[(df['Continent'] == 'North America') ]#& (df['Continent'] == 'South America')]
df3

df4 = df.loc[(df['Continent'] == 'South America') ]
df4

df5 = pd.concat([df3,df4],axis=0)
df5

df5 = df5['GDP (millions of US$)']
df5

t_statistic2 , p_value2 = scipy.stats.ttest_ind(df2,df5,equal_var=False)
t_statistic2,p_value2
