#大佬之间的差距
import pandas as pd

Nowcoder = pd.read_csv('Nowcoder.csv', sep=',')
print(int(Nowcoder[Nowcoder['Level']==7]['Achievement_value'].max()-Nowcoder[Nowcoder['Level']==7]['Achievement_value'].min()))



#import pandas as pd
#from numpy import maximum
#fileName='Nowcoder.csv'
#df=pd.read_csv(fileName,sep=',')
#c=df.query("Level == 7")#筛选出等级为7的人的信息
#k=c["Achievement_value"]#筛选出他们的成就值
#g=max(k)-min(k)#用最大值函数和最小值函数进行相减
#print(g)
