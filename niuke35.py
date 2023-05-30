import pandas as pd 
df=pd.read_csv('Nowcoder.csv',sep=',') 
print(df.groupby('Graduate_year').Achievement_value.max())