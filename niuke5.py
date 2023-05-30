#用户没有补全的信息（isnull: 判断是否为空。）
import pandas as pd
Nowcoder = pd.read_csv('Nowcoder.csv',sep=',',dtype=object)
print(Nowcoder.isnull().any(axis=0))
#isnull: 判断是否为空。
     #  返回bool类型的值：True or False
#any：返回是否至少一个元素为真
   #    all：返回是否所有元素为真
    #   axis=1或0:    1表示横轴，方向从左到右；0表示纵轴，方向从上到下
