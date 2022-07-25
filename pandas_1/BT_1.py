
import pandas as pd
import numpy as np
# 1
data=pd.read_csv('data\GDPlist.csv', encoding= 'unicode_escape')#đọc dữ liệu

data.shape[0] # số dòng

data.shape[1] # số cột


# 2
#đổi tên cột
data.rename(columns={'Country':'nuoc','Continent':'chauluc','GDP (millions of US$)':'GDP( trieu $)'},inplace=True)

# # 3
data.insert(1,'Thanhpho',data.loc[:,'nuoc'])

# # 4
data['Thanhpho'].replace('Vietnam','hanoi',inplace=True)


# 5
vitri = data.loc[data.chauluc == 'Asia'].index
data.drop(vitri,axis=0,inplace=True)

# 6

vitri = data.loc[data['GDP( trieu $)'] < 300000].index

