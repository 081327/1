#统计远动会项目报名人数
import pandas as pd 

df1 = pd.read_csv('items.csv')
df2 = pd.read_csv('signup.csv')

df = df1.merge(df2,left_on='item_id', right_on='item_id')
data = df.groupby(by='item_name')['employee_id'].nunique()

print(data)

#nunique()与unique()的区别

#nunique()返回的类型是数值

#unique()返回的类型是ndarray
#很明显是按列合并，观察两张表，都有相同的字段'item_id'

#df = df1.merge(df2,left_on='item_id', right_on='item_id') 将两张表合并（注意是内链接）