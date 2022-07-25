import pandas as pd

data = pd.read_csv('data\OnlineRetail.csv',encoding='unicode_escape')
data.info() #kiểu dữ liệu của các thuộc tính
data.shape #số dòng, số cột
#Trích xuất dữ liệu các cột Description và Quantity lưu vào file OnlineRetail.csv
data.loc[:,['Description','Quantity']].to_csv('Onlineretail.csv')

#Trích xuất dữ liệu 1000 dòng đầu tiên lưu vào file OnlineRetail.xlsx
data.loc[:999].to_excel('Onlineretail.xlsx')

#Trích xuất các bản ghi có số lượng từ 10 trở lên lưu vào file OnlineRetail.h5
data.loc[data.Quantity > 10].to_hdata('Onlineretail.h5',key='data')

#Trích xuất dữ liệu các phần tử từ dòng 1000 đến dòng 2000, các cột Quantity, InvoiceDate, UnitPrice lưu vào file OnlineRetail.json
data.loc[999:1999,['InvoiceDate','Quantity','UnitPrice']].to_json('Onlineretail.json')

#Trích xuất các bản ghi có số hóa đơn ‘536365’ lưu vào file OnlineRetail.html
data.loc[:,data.InvoiceNo == 536365].to_html('Onlineretail.html')







