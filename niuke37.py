import pandas as pd 
Nowcoder = pd.read_csv('Nowcoder.csv', sep=',') 
a=Nowcoder.groupby(by=['Level'])['Nowcoder_ID'].count() 
b=a[a>5] #注意：这块将a>5的放在一个列表中，然后输出
print(b)