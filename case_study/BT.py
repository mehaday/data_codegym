import pandas as pd 
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split
import seaborn as sns
from  sklearn.metrics import mean_absolute_percentage_error
from scipy.stats import f_oneway


# mse: 8030585.752891239
# mse: 7257257.505197483

# "carname": 536275.1656468532

# mape
def normalize(df):
    max_column  = df.max()
    min_column  = df.min()
    df_nor = (df - df.min()) / (df.max()-df.min())
    return max_column, min_column, df_nor

df = pd.read_csv("data\Case_study_CarPrice_Assignment.csv")

# feature_process = ["car_ID","CarName","fueltype", "aspiration", "doornumber",
#              "carbody","drivewheel","enginelocation","enginetype","cylindernumber", "fuelsystem"]

# df = df.drop(feature_process, axis=1)

# # chon lua x cac feature to


# df_feature = df.loc[:, df.columns != 'price']
# norm
df['carlength'] = df['carlength']/df['carlength'].max()
df['carwidth'] = df['carwidth']/df['carwidth'].max()
df['carheight'] = df['carheight']/df['carheight'].max()

# categorical

# df['fueltype'] = df['fueltype'].astype('category')
# df['carbody'] = df['carbody'].astype('category')
# df['drivewheel'] = df['drivewheel'].astype('category')



print(df.shape)


features =["carlength", "carwidth", "carheight", "fueltype", "drivewheel",
            "carbody", "enginesize", "price", "CarName", "symboling", "aspiration","horsepower","peakrpm","highwaympg","compressionratio","enginelocation"]


df_target = df[features]
# category = one-hot
df_target = pd.get_dummies(df_target, columns =["fueltype", "carbody", "drivewheel", "CarName","symboling","aspiration","enginelocation"], dummy_na=True)


y = df_target["price"]
X = df_target.drop("price", axis=1)


# # chia du lieu 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


reg = LinearRegression().fit(X_train, y_train)
# 
# a = reg.coef_
# b = reg.intercept_

# # metrics
pred = reg.predict(X_test)
print(mean_squared_error(y_test, pred))
print(mean_absolute_percentage_error(y_test, pred))


# sns.regplot(x ='enginesize', y ='price', data = df_target)
# plt.ylim(0, )
# plt.show()

#####################################


print(list(df_target.columns))

# ANOVA(p_value <0.05 chap nhan H0 bac bo H1)
statistics = f_oneway(df_target.loc[:,"enginelocation_rear"], df_target.loc[:,"price"])
print(statistics)