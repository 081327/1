#修补缺失的用户数据
#法一：主要使用键值对的形式
import pandas as pd

Nowcoder = pd.read_csv('Nowcoder.csv', sep=',')
pd.set_option('display.width', 300)  # 设置字符显示宽度
pd.set_option('display.max_rows', None)  # 设置显示最大行
pd.set_option('display.max_columns', None)

max_year = Nowcoder.Graduate_year.max()
mean_ach = Nowcoder.Achievement_value.mean()
#存入键值对的情况，赋值给后面
values = {"Graduate_year":max_year,
          "Language":'Python',
          "Achievement_value":mean_ach
         }
# false的情况，此时Nowcoder的值没有变化，new_table存储新值
new_table = Nowcoder.fillna(value=values)
print(new_table)  #这块要注意，没有替代就证明生成了个新表
# True的情况，此时Nowcoder的值已经变化
Nowcoder.fillna(value=values,inplace=True)
print(Nowcoder)   #替代表示还是原来的表


#法二：不用键值对，直接赋值的形式
import pandas as pd
# 读取csv文件, sep指定列分隔符
Nowcoder = pd.read_csv("Nowcoder.csv", sep=",")
# 设置打印选项,以显示全部列
pd.set_option("display.width", 300)
# 设置显示所有行
pd.set_option("display.max_rows", None)
# 设置显示所有列
pd.set_option("display.max_columns", None)



# 用Graduate_year列的最大值填充Na值
Nowcoder.Graduate_year.fillna(Nowcoder.Graduate_year.max(), inplace=False)
# 用Python填充Language列的Na值
Nowcoder.Language.fillna("Python", inplace=False)
# 用Achievement_value列的平均值(四舍五入)填充Na值
Nowcoder.Achievement_value.fillna(
    Nowcoder.Achievement_value.mean().round(0), inplace=False
)       #round(0)表示四舍五入到整数位
# 打印数据
print(Nowcoder)
