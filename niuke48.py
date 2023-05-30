import pandas as pd
sales = pd.read_csv('sales.csv')
R = pd.qcut(sales["recency"], 4,labels=["4", "3", "2", "1"]).astype("str")
F = pd.qcut(sales["frequency"], 4, labels=["1", "2", "3", "4"]).astype("str")
M = pd.qcut(sales["monetary"], 4, labels=["1", "2", "3", "4"]).astype("str")
sales['RFMClass'] = R+F+M
print(sales.head(5))
print('\n')
print(sales[sales['RFMClass'] == '444'].sort_values('monetary',ascending= False).head(5))