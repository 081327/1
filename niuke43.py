# 导入Pandas库
import pandas as pd

# 设置pandas显示配置,以显示完整的数据框
pd.set_option("display.width", 300)
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)

# 读取Nowcoder1.csv文件
Nowcoder1 = pd.read_csv("Nowcoder1.csv")

# 读取Nowcoder2.csv文件
Nowcoder2 = pd.read_csv("Nowcoder2.csv")

# 使用pd.merge()进行内连接,以Nowcoder_ID作为键
df = pd.merge(Nowcoder1, Nowcoder2, how="inner", on="Nowcoder_ID")

# 打印结果
print(df)
