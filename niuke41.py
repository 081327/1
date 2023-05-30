import pandas as pd
items = pd.read_csv('items.csv',sep = ',')
signup = pd.read_csv('signup.csv',sep = ',')

# 第一步连接两个表，默认内连接就可以
df = pd.merge(left = items,right = signup,on = 'item_id')

# 限定同时满足两个条件，注意item_name是javelin，题目里写错了多了一个n,坑死了！之前复制一直报错
df1 = df[(df['department'] == 'functional')&(df['item_name'] == 'javelin')]

print(df1[['employee_id','name','sex']].reset_index(drop = True)) 
# 注意重置索引
# reset_index用来重置索引，因为有时候对dataframe做处理后索引可能是乱的。
# drop=True就是把原来的索引index列去掉，重置index。
# drop=False就是保留原来的索引，添加重置的index。
# 两者的区别就是有没有把原来的index去掉
