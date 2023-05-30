#用分位数分析牛客网用户活动
#pd.quantile()为求分位数操作，需要自行在里面添加数值
import pandas as pd

Nowcoder = pd.read_csv('Nowcoder.csv', sep=',')
print(Nowcoder[['Achievement_value','Continuous_check_in_days']].quantile(q=0.25))
print(Nowcoder[['Num_of_exercise','Number_of_submissions']].quantile(q=0.75))