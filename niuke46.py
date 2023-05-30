# 导入Pandas库
import pandas as pd

# 读取Nowcoder.csv文件
Nowcoder = pd.read_csv("Nowcoder.csv")

# 设置显示宽度为300
pd.set_option("display.width", 300)

# 显示所有列,默认只显示20列
pd.set_option("display.max_columns", None)

# 显示所有行,默认只显示60行
pd.set_option("display.max_rows", None)

# 对Level列升序排序
Nowcoder = Nowcoder.sort_values(by="Level")

# 打印排序后的结果
print(Nowcoder)
