

import pandas as pd 
Nowcoder = pd.read_csv('Nowcoder.csv',sep=',')
print(Nowcoder.groupby(['Level','Language'])['Nowcoder_ID'].sum())
