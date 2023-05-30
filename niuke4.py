#统计部分用户使用语言
import pandas as pd
Nowcoder = pd.read_csv('Nowcoder.csv',sep=',',dtype=object)
# print(Nowcoder['Language'].iloc[10:21])
# print(Nowcoder['Language'].loc[10:20])
# print(Nowcoder.iloc[10:21,5])
print(Nowcoder.loc[10:20,'Language'])   #前面输入行信息，10-20行；后面输入列信息；