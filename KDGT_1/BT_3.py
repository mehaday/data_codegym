# [Bài tập] Kiểm định giả thuyết trên bộ dữ liệu credit scoring

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.preprocessing import StandardScaler
import scipy

df = pd.read_csv('data/Credit_Scoring.csv')
df.head()

df.columns

df.info()

# KIểm Định giả thuyết

df1 = df[['MonthlyIncome','NumberOfDependents']]
df1

condition = (  df1.MonthlyIncome.isna() | df1.NumberOfDependents.isna() )

df1 = df1[condition==False]
df1

t_statistic5 , p_value5 = scipy.stats.ttest_ind(df1[df1['NumberOfDependents']==1]['MonthlyIncome'],df1[df1['NumberOfDependents']==2]['MonthlyIncome'],equal_var=False)
t_statistic5,p_value5


df2 = df[['NumberOfOpenCreditLinesAndLoans','SeriousDlqin2yrs']]
df2

df2['SeriousDlqin2yrs'].unique()

condition1 = (  df2.NumberOfOpenCreditLinesAndLoans.isna() | df2.SeriousDlqin2yrs.isna() )

df2 = df2[condition1 == False]
df2

t_statistic6 , p_value6 = scipy.stats.ttest_ind(df2[df2['SeriousDlqin2yrs']==1]['NumberOfOpenCreditLinesAndLoans'],df2[df2['SeriousDlqin2yrs']==0]['NumberOfOpenCreditLinesAndLoans'],equal_var=False)
t_statistic6,p_value6