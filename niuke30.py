#每日练题量
#使用groupby按照date分组，聚合函数count统计题目数量
import pandas as pd
nowcoder = pd.read_csv('nowcoder.csv', parse_dates=True, index_col='date')   #parse_dates=True表示尝试解析index为日期格式，索引形式为日期索引
daily_num = nowcoder.groupby('date')['question_id'].count()
print(daily_num)