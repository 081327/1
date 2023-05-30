#用pandas查看用户数据

#pandas是python的一个数据库，在使用数据库的时候需要输入 import pandas as pd 引入，
#df = pd.read.csv(''文件路径“）：这是利用pandas数据库读取CSV文件的方法，如果读取EXCEL文件或者其他文件，csv文件换成其他文件的格式。
#df.dtypes:如果在文件中有字符型数据返回object
#df.head(n):表示将前n行数据显示出来，默认是显示前五行
#df.tail(n):表示将后n行数据显示出来，默认后五行
#最后打印即可

import sys

import pandas as pd    #导入pandas数据库

data = pd.read_csv("Nowcoder.csv",dtype=object)    #dtype=object是防止读取为小数

cols = [
    "Nowcoder_ID",
    "Level",
    "Achievement_value",
    "Num_of_exercise",
    "Graduate_year",
    "Language",
]

data_filter = data[cols]

print(data.head(6))  #前6行显示出来

