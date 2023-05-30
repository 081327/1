#用户最近的最长与最短连续签到天数
import pandas as pd

Nowcoder = pd.read_csv('Nowcoder.csv', sep=',')
print(Nowcoder['Continuous_check_in_days'].max())
print(Nowcoder['Continuous_check_in_days'].min())