import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('data\FoodPrice_in_Turkey.csv', encoding= 'unicode_escape')

data.info()

# Giá trung bình của từng loại thực phẩm
TB_ThucPham = data.groupby('ProductName').mean()

print(TB_ThucPham)