#用户等级的中位数
#中位数   median（）







import pandas as lie
# 这里题目邀请：直接输出计算的中位数，输出类型为整型Int。打开文件不要设置int
# s = lie.read_csv("Nowcoder.csv", sep=",", dtype=int)
s = lie.read_csv("Nowcoder.csv", sep=",")
k = s["Num_of_exercise"] >= 10
c = s[k]['Level'].median()
print(int(c))   #注意这块必须输出为整数，别忘记加int（）
