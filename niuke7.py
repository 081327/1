#python用户的成就值
import pandas as pd
 
data  = pd.read_csv("Nowcoder.csv", dtype=object)
print(data[data['Language']=='Python']['Achievement_value'])

#print(df[df["Language"]=="Python"].loc[:,"Achievement_value"])