#解决用户重复的数据
#duplicated()是对整行进行查重，return 重复了的数据，且只现实n-1条重复的数据（n是重复的次数）
#说明drop_duplicates()函数是将所有重复的数据都去掉了，且默认保留重复数据的第一条。



# 导入pandas库
import pandas as pd

# 读取Nowcoder.csv文件,得到DataFrame
nowcoder = pd.read_csv("Nowcoder.csv")

# 检查nowcoder中的重复行,返回布尔型列表
nowcoder_duplicated = nowcoder.duplicated()

# 删除nowcoder中的重复行
nowcoder_nodupicated = nowcoder_duplicated.drop_duplicates()

# 输出nowcoder_duplicated结果
print(nowcoder_duplicated)

# 输出nowcoder_nodupicated结果
print(nowcoder_nodupicated)
