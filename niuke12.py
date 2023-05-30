#按照毕业年份与使用语言筛选7级用户
import pandas as pd

Nowcoder = pd.read_csv('Nowcoder.csv', sep=',')
pd.set_option('display.width', 300) # 设置字符显示宽度
pd.set_option('display.max_rows', None) # 设置显示最大行
pd.set_option('display.max_columns', None)
cond1 = Nowcoder['Language'] == 'CPP'
cond2 = Nowcoder['Level'] == 7
cond3 = Nowcoder['Graduate_year'] != 2018
cond = cond1 & cond2 & cond3
print(Nowcoder[cond])