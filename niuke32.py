#每日正确与错误的答题次数
import pandas as pd

df = pd.read_csv('nowcoder.csv', sep=',')

df['year-month-day'] = pd.to_datetime(df['date']).dt.date  # 如果df表中没有'year-month-day'字段列，则新建一个该字段列

num = df.groupby(['result','year-month-day'])['result'].count() # 分组聚合运算，两个字段作为分组依据，对对应结果进行聚合运算

print(num)

