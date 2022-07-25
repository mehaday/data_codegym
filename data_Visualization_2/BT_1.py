import pandas as pd
import matplotlib.pyplot as plt
import datetime
import seaborn as sns


# [Bài tập] Vẽ biểu đồ kết hợp – GDP list


import pandas as pd
import matplotlib.pyplot as plt
import datetime
import seaborn as sns


df = pd.read_csv('data/GDPlist.csv',encoding='ISO-8859-1')
df

# Biểu đồ để hiển thị giá trị cụ thể và so sánh GDP các nước Vietnam,  Indonesia, Cambodia, Thailand và Malaysia.


df['Country']=df['Country'].str.strip()


df1=df[(df['Country']=='Vietnam') | (df['Country']=='Indonesia') | (df['Country']=='Cambodia') | (df['Country']=='Thailand') | (df['Country']=='Malaysia')]
df1


import plotly.express as px
fig = px.bar(df1, x='Country', y='GDP (millions of US$)')
fig.show()

# Biểu đồ để đánh giá tỉ lệ đóng góp GDP của các nước trên tổng số GDP của 5 nước Vietnam,  Indonesia, Cambodia, Thailand và Malaysia.


from matplotlib.pyplot import figure
figure(figsize=(16, 9), dpi=80)
myexplode = [0, 0, 0, 0,0.2]
plt.pie(df1['GDP (millions of US$)'],labels=df1['Country'],explode=myexplode,autopct='%1.2f%%', radius=1.3)
plt.legend(title='GDP of VietNam in South East Asia')
plt.show()


