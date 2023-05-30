#python用户平均提交次数
#mean（）表示求平均数，一组结果的中值

import pandas as pd

Nowcoder = pd.read_csv('Nowcoder.csv', sep=',')
# df = Nowcoder[Nowcoder.Language == 'Python']
# result = df.Number_of_submissions.mean()
# print(round(result,1))

print(round(Nowcoder[Nowcoder.Language=='Python']['Number_of_submissions'].mean(),1))