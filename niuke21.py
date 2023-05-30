#方差与标准差
#方差；var（）
#标准差：std（）
import pandas as pd

Nowcoder = pd.read_csv('Nowcoder.csv', sep=',')
print(round(Nowcoder.Num_of_exercise.var(),2))#刷题量的方差
print(round(Nowcoder.Number_of_submissions.std(),2))#提交代码次数的标准差