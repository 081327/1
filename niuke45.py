import pandas as pd
sales = pd.read_csv('sales.csv')
#注意：后面[:3]指的是从0开始索引，前三个0，1，2
data = sales.sort_values(by='monetary', ascending=False).reset_index(drop=True)[:3]
print(data)
#对于值排名，使用函数df.sort_values(by= , axix=,ascending= , inplace=,na_postion=)。

#注意： by参数指定要排序的列，
 #           axis=0表示按照行进行排名，axis=1表示按照列进行排名，默认0；
  #          ascending=True表示升序，ascending=False表示降序，默认True.
   #         inplace 代表是否要更改原数据，true代表修改原数据。false代表新建副本，在副本修改
    #        na_position参数用于设定缺失值的显示位置，first表示缺失值显示在最前面,last表示缺失值显示在最后面
#reset_index用来重置索引，因为有时候对dataframe做处理后索引可能是乱的。

#drop=True就是把原来的索引index列去掉，重置index。

#drop=False就是保留原来的索引，添加重置的index。