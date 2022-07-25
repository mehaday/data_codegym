import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data/OnlineRetail.csv',encoding='unicode_escape')
data.dtypes
data.shape


data.pivot_table(values='Quantity',index='InvoiceNo',columns='Country',aggfunc='mean')


data.pivot_table(values='Quantity',index='CustomerID',columns='StockCode',aggfunc='max')
data.pivot_table(values='Quantity',index='CustomerID',columns='StockCode',aggfunc='min')

