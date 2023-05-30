#牛客网不同语言使用人数
#value_counts()根据计算结果默认降序排序
import pandas as pd
df = pd.read_csv("Nowcoder.csv")
print(df.Language.value_counts())