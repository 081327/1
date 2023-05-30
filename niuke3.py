#第十位用户
import sys

import pandas as pd

data = pd.read_csv("Nowcoder.csv",dtype=object)#防止读取为小数

cols = [
    "Nowcoder_ID",
    "Level",
    "Achievement_value",
    "Num_of_exercise",
    "Graduate_year",
    "Language",
]

data_filter = data[cols]


print(data_filter.loc[10,:])    #查找位置，主要用到loc函数，前面输入行，后面输入列，这里后面没有写，证明输出第10行的所有内容
#iloc :  Selection by Position，即按位置选择. 只接受整型参数。  
#不接受列字段名称作为参数，只支持列字段的位置索引作为参数。