#统一最后刷题日期的格式
#to_datetime函数该函数可以将字符型的时间数据转换为时间型数据
import pandas as pd
Nowcoder = pd.read_csv("Nowcoder.csv", sep=",", dtype=object)  # 要设置sep,dtype
Nowcoder["Last_submission_time"] = pd.to_datetime(
    Nowcoder["Last_submission_time"], format=("%Y-%m-%d")
)#python索引列一定要带表格索引(包括赋值)
#pandas有专门的的日期格式化函数
print(Nowcoder.loc[:, ["Nowcoder_ID", "Level", "Last_submission_time"]])
