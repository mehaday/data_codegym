import pandas as pd
import seaborn as sns

df = pd.read_csv("FoodPrice_in_Turkey.csv")
df.info()

df.describe()

df = df.dropna()

sns.violinplot(y = "Price", data=df)

sns.countplot(x = "Year", data = df)

sns.boxplot(x=df["Price"])