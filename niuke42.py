import pandas as pd 

items = pd.read_csv('items.csv')
signup = pd.read_csv('signup.csv')

data = items.merge(signup,on='item_id')

table = pd.pivot_table(
               data,
               columns=['item_name'],
               index=['sex', 'department'],
               values=["employee_id"],
               aggfunc='count',
               fill_value=0)
               
print(table)


#pandas.pivot_table透视表各参数含义：
#data：待操作的 DataFrame
#values：被聚合操作的列，可选项
#aggfunc：聚合函数/函数列表，默认 numpy.mean 这里要注意如果 aggfunc 中存在函数列表，则返回的 DataFrame 中会显示函数名称
#fill_value：默认 None，可设定缺省值
#dropna：默认 True，如果列的所有值都是 NaN，将被删除；False 则保留
#margins：默认 False，设置为 True 可以添加行/列的总计
#margins_name：默认显示 'ALL'，当 margins = True 时，可以设定 margins  行/列的名称