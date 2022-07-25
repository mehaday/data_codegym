import pandas as pd
from scipy import  stats

df = pd.read_csv("shopeep_koreantop_clothing_shop_data.csv", encoding="UTF-8")

df1 = df.filter(["rating_star", "follower_count"])
df1 = df1.dropna()
print(stats.pearsonr(df1.rating_star, df1.follower_count))

