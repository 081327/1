#将用户的json文件转化成表格形式

#法一
import pandas as pd
import json

pd.set_option('display.width', 300)  # 设置字符显示宽度
pd.set_option('display.max_rows', None)  # 设置显示最大行
pd.set_option('display.max_columns', None)


#下面重点
with open('Nowcoder.json', 'r') as f:    #只读模式打开文件
    data = json.loads(f.read())          #加载读取信息赋值给变量
print(pd.DataFrame(data))                #信息转化为数据框



#法二
import pandas as pd

df = pd.read_json('Nowcoder.json', dtype=dict)

pd.set_option('display.width', 300)  # 设置字符显示宽度
pd.set_option('display.max_rows', None)  # 设置显示最大行
pd.set_option('display.max_columns', None)

print(pd.DataFrame(df))
