#qcut函数:可以根据样本分位数对数据进行面元划分。
#pd.qcut函数，按照数据出现频率百分比划分，比如要把数据分为四份，则四段分别是数据的0-25%，25%-50%，50%-75%，75%-100%，每个间隔段里的元素个数都是相同的。 
#pd.qcut(x, q, labels=None, retbins=False, precision=3, duplicates='raise') #最后一个参数 duplicates='drop'表示若有重复区间则删除 
#使用astype()将纯数字组成的字符串修改成int

import pandas as pd 
sales=pd.read_csv('sales.csv')
sales['R_Quartile']=pd.qcut(sales.recency,4,labels=[4,3,2,1]).astype("int")
sales['F_Quartile']=pd.qcut(sales.frequency,4,labels=[1,2,3,4]).astype("int")
sales['M_Quartile']=pd.qcut(sales.monetary,4,labels=[1,2,3,4]).astype("int")
print(sales.head())
