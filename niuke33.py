import pandas as pd
nowcoder = pd.read_csv('nowcoder.csv')
result_df = nowcoder.groupby('result')
print(result_df.size())
#count把每一列的值都返回出现的次数
#size表示分组字段的出现次数