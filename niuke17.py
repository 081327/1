#用户常用语言有多少
# 使用.unique()获取Language一列不同语言的名称
# 使用.nunique()获取Language一列不同语言的数量
import pandas as pd
 
df =pd.read_csv('Nowcoder.csv')
res = df.Language.unique()  #返回ndarray类型
print(len(res))
print(res)



# 导入pandas库
#import pandas as pd

# 读取Nowcoder.csv数据集
#nowcoder = pd.read_csv("Nowcoder.csv")

# 使用.nunique()获取Language一列不同语言的数量
#language_number = nowcoder["Language"].nunique()

# 使用.unique()获取Language一列不同语言的名称
#language_names = nowcoder["Language"].unique()

# 打印语言数量与名称
#print(language_number, "\n", language_names)
