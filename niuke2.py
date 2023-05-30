#用户数据集的大小


#法一
import pandas as pd
 
a = pd.read_csv('Nowcoder.csv',dtype=object)
# .read_csv可以直接读取文件的行数，利用len（）直接得到长度即文件行数
total_lines = len(a)  #读取行数直接len（a）就行
# 利用.columns获取列，用len（）得到具体总列数
total_cloumn = len(a.columns)   #读取列数用到len（a.columns）
print((total_lines,total_cloumn))

#法二
import pandas as pd 
data = pd.read_csv('Nowcoder.csv') 
print(data.shape) 
#df.shape输出数据框的行数和列数
#df.info()输出数据框各列的数据格式
#df.describe()输出数据框的统计特征