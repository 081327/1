#去掉信息不全的用户
import pandas as pd
# import numpy as np
d = pd.read_csv('Nowcoder.csv',dtype='object')
pd.set_option('display.width',300)
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
print(d.dropna(axis=0,how='any'))   
#dropna函数功能是专门用来删除列表，数据框或系列中缺失/NaN值的
#dropna函数后面括号能设置参数，
# 1、axis：可以设置为0，表示按照行（axis=0）或列（axis=1）来丢弃数据
#2、how：可以设置为all或any，用于指定要求行或列中空值/NaN值的数量，all表示全部为控制则被丢弃，any表示只要有一个空值就被丢弃
#3、inplace：可以设置为True或False，用于决定是将结果直接写入原表格还是返回一个新的表格，如果inplace=True，则不返回新的表格，直接在传入的
#表格上进行操作，而inplace=False，则会返回一个新的表格，原表格保持不变

