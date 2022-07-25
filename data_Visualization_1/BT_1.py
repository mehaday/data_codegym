import pandas as pd
import matplotlib.pyplot as plt
import seaborn

df=pd.read_csv('data/GDPlist.csv',encoding='ISO-8859-1')

df.head()


df.isnull()


# # So sánh GDP các nước ở South America.


df1=df[df['Continent']=='South America']
df1


from matplotlib.pyplot import figure
figure(figsize=(16, 9), dpi=80)
plt.bar(df1['Country'], df1['GDP (millions of US$)'], width = 0.5)
plt.title('GDP in South America', fontsize = 16, color = 'r')
plt.xlabel('Country', fontsize = 14)
plt.ylabel('GDP', fontsize = 14)
plt.show()


# # **Đánh giá tỉ lệ đóng góp GDP của Việt Nam trên tổng số GDP của 5 nước Đông Nam Á là Vietnam,  Indonesia, Cambodia, Thailand và Malaysia.**


df2=df[df['Continent']=='Asia']
df2


df2['Country']=df2['Country'].str.strip()


df3=df2[(df2['Country']=='Vietnam')]
df4=df2[(df2['Country']=='Cambodia')]
df5=df2[(df2['Country']=='Malaysia')]
df6=df2[(df2['Country']=='Indonesia')]
df7=df2[(df2['Country']=='Thailand')]


df9=df2[(df2['Country']=='Vietnam') | (df2['Country']=='Indonesia') | (df2['Country']=='Cambodia') | (df2['Country']=='Thailand') | (df2['Country']=='Malaysia')]
df9


df4


from matplotlib.pyplot import figure
figure(figsize=(16, 9), dpi=80)
myexplode = [0, 0, 0, 0,0.2]
plt.pie(df9['GDP (millions of US$)'],labels=df9['Country'],explode=myexplode)
plt.legend(title='GDP of VietNam in South East Asia')
plt.show()
