#大佬用户成就值比例
import pandas as pd

Nowcoder = pd.read_csv('Nowcoder.csv', sep=',')
seven=Nowcoder[Nowcoder['Level']==7]['Achievement_value']#筛选出7级用户的成就值
total=Nowcoder['Achievement_value'].sum()#计算出所有用户的成就值之和
print(seven/total)