#查看哪些用户使用python
import pandas as pd
Nowcoder = pd.read_csv('Nowcoder.csv',sep=',',dtype=object)
cond = Nowcoder['Language'] == 'Python'
print(Nowcoder[cond])