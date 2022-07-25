# Bài tập] Kiểm định tương quan của các thuộc tính trên bộ dữ liệu house price Đống Đa**

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.preprocessing import StandardScaler
import scipy

data = pd.read_csv('data\house_price_Dống-Da_Hà-Nội_subdata.csv')
data.head()

# Giữa giá nhà và diện tích có tương quan với nhau?

