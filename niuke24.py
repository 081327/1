#统计用户名字的长度
import pandas as pd

Nowcoder = pd.read_csv('Nowcoder.csv', sep=',')
print(Nowcoder['Name'].str.len())#方法一

#另一种解法
# 导入pandas库
#import pandas as pd
 
# 读取Nowcoder.csv文件,得到DataFrame
#nowcoder = pd.read_csv("Nowcoder.csv")
 
# 获取Name列
#names = nowcoder["Name"]
 
# 计算Name列中每个字符串的长度
#names_len = names.str.len()
 
# 输出字符串长度的Series
#print(names_len)
