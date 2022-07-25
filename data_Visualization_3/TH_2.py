import pandas as pd
import seaborn as sns

df = pd.read_csv("OnlineRetail.csv", encoding = "ISO-8859-1")
df.info()

df.describe()

df = df.dropna()

df["Price"] = df["Quantity"] * df["UnitPrice"]

sns.violinplot(y = "UnitPrice", data=df)

df2 = df.groupby(['InvoiceNo'])['Quantity'].sum().reset_index()
df2.head()

df3 = df.groupby(['Country'])['Quantity'].sum().reset_index()
df3.head()

df1 = df.drop_duplicates(subset = 'InvoiceNo')
sns.countplot(x = "Country", data = df1)
