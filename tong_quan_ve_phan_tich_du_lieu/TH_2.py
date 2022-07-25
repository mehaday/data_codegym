import pandas as pd
data=pd.read_csv('data\OnlineRetail.csv', encoding = "ISO-8859-1")
# hiển thị 5 dòng dữ liệu đầu tiên
data.head()

# cấu trúc bộ dữ liệu
print (data.info())

# lấy ra tên các quốc gia
country = data.Country.unique()
print ("số lượng các quốc gia: " + str(country.size))

# Tạo cột tính thành tiền của các mặt hàng
data['total'] = data['Quantity'] * data['UnitPrice'] 

# Giá trị đơn hàng của mỗi đơn hàng
total_invoices = data['total'].sum()
print ("số lượng hóa đơn bán ra: "+ str (total_invoices.size))
print ("Tổng doanh thu: " + str(total_invoices.sum()))