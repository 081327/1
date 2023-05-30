#用户最高的正确率
import pandas as pd
Nowcoder = pd.read_csv('Nowcoder.csv', sep=',')
a=Nowcoder.query('Num_of_exercise>10')['Num_of_exercise']
#注意query参数带引号
b=Nowcoder.query('Num_of_exercise>10')['Number_of_submissions']
x=a/b
print(round(x.max(),3))