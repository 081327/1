#刷题量大于500的
import pandas as pd
Nowcoder = pd.read_csv('Nowcoder.csv',sep=',')
cond = Nowcoder['Num_of_exercise'] >= 500
print(Nowcoder[cond][['Level','Achievement_value']])




#法二

#import pandas as pd
 
# 从当前目录读取Nowcoder.csv数据集
#Nowcoder = pd.read_csv("Nowcoder.csv")
# 过滤刷题数量大于500题的用户
# 存储结果在high_exercise变量中
#high_exercise = Nowcoder[Nowcoder["Num_of_exercise"] > 500]    记得一定要用中括号[]
# 提取high_exercise中的Level和Achievement_value两列
# 存储在level_achievement变量中
#level_achievement = high_exercise[["Level", "Achievement_value"]]
# 打印level_achievement变量
#print(level_achievement)
