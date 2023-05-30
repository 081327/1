# 导入Pandas库
import pandas as pd

# 读取Nowcoder1.csv文件
Nowcoder1 = pd.read_csv("Nowcoder1.csv")

# 读取Nowcoder2.csv文件
Nowcoder2 = pd.read_csv("Nowcoder2.csv")

# 使用pd.merge()进行内连接,以Nowcoder_ID作为键
Nowcoder_all = pd.merge(Nowcoder1, Nowcoder2, how="inner", on="Nowcoder_ID")

# 选择Name、Num_of_exercise和Number_of_submissions三列
name_exercise_submission = Nowcoder_all[["Name", "Num_of_exercise", "Number_of_submissions"]]

# 打印结果
print(name_exercise_submission)
