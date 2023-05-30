#2020年毕业的人中最喜欢用Java的用户
#这里用到了set_option主要是做一些标注和图例
import pandas as pd
Nowcoder = pd.read_csv('Nowcoder.csv',sep=',')
pd.set_option('display.width', 300) # 设置字符显示宽度
pd.set_option('display.max_rows', None) # 设置显示最大行
pd.set_option('display.max_columns', None)
print(Nowcoder.loc[(Nowcoder['Language']=='Java')&(Nowcoder['Graduate_year']==2020),:])