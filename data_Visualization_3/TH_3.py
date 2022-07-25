import pandas as pd
import seaborn as sns

df = pd.read_csv("GDPlist.csv", encoding = "ISO-8859-1")

df.info()

df = df.dropna()

sns.violinplot(y=df["GDP (millions of US$)"])

sns.violinplot(y=df[df["Continent"]=="Asia"]["GDP (millions of US$)"])

sns.boxplot(x="Continent", y = "GDP (millions of US$)", data=df)

