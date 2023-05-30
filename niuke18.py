#最多的用户等级
#pd.mode是求众数的函数
import pandas as pd

Nowcoder = pd.read_csv('Nowcoder.csv', sep=',')
print(Nowcoder.loc[:,['Level']].mode())
# print(Nowcoder.iloc[:,[1]].mode())
# print(Nowcoder[['Level']].mode())
# res = Nowcoder['Level'].mode()
# print(pd.DataFrame(res,columns = ['Level']))