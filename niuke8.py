#文件最后用户的部分数据
import pandas as pd

df = pd.read_csv("Nowcoder.csv",sep=",")
# print(df.iloc[-5:,[0,1,2,5]])
# print(df.tail(5).iloc[:,[0,1,2,5]])
print(df.iloc[-5:][['Nowcoder_ID', 'Level', 'Achievement_value', 'Language']])
