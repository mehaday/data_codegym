import pandas as pd
import numpy as np

ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]

# định nghĩa khoảng giá trị các nhóm
bins = [18, 25, 35, 60, 100]

# thực hiện rời rạc hóa
cats = pd.cut(ages, bins)

# lấy ra index của nhóm tương ứng với các phần tử
cats.codes

# lấy ra các nhóm
cats.categories

# thống kê số lượng phần tử ở mỗi nhóm
pd.value_counts(cats)

pd.cut(ages, [18, 26, 36, 61, 100], right=False)


# danh sách nhãn
group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']

pd.cut(ages, bins, labels=group_names)