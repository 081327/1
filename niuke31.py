#用户练习的平均次日留题率
import pandas as pd
# 读文件
df = pd.read_csv('nowcoder.csv', sep=',')
# 转换日期格式
df['date'] = pd.to_datetime(df['date']).dt.date # .dt.date得到精确到天的日期
# 拷贝原表于新表df1
df1 = df.copy()
# 将新表的时间+1天（往后推一天）
df1['date'] = df1['date'] + pd.Timedelta(days=1)
# 将原表df和新表合并得到新表total，内连接取交集，键/连接字段 是 userid和date
total = pd.merge(df,df1, how='inner', on=['user_id','date'])
# 统计合并后剩下的第二天还会再来练习的人数n
n = total['user_id'].count()
# 统计原表中的用户数n1
n1 = df['user_id'].count()
# 计算次日留存率
print(round(n / n1 ,2))
