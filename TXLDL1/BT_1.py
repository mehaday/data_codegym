
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("OnlineRetail.csv")
df

df.info()

df.describe()

df.isna()


df['Description'] = df['Description'].fillna('Không biết', inplace=True)


c=0
for i in df['Description']:
    if i == 'Không biết':
        c = c+1
print(c)


# tính giá trị Q1 và Q3
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3-Q1
print(Q1, Q3, IQR)


# lọc dữ liệu ngoại lai
df2 = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]
df2.boxplot()

sns.boxplot(df2["Quantity"])


sns.boxplot(df2["UnitPrice"])


df2.describe()

