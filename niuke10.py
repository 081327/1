#牛客网C系用户们的信息

#1、query（）函数查找Languague列中的CPP、C
#2、直接在Languague中查找是否是CPP、C，也可以用loc函数差查找
#3、isin()函数：用来清洗数据，删选过滤掉Dateframe中的一些行，直接用返回的是bool值，然后放入Nowcoder[  {内容} ]中，则返回返回为True的数据行


import pandas as pd
Nowcoder = pd.read_csv('Nowcoder.csv',sep=',')
pd.set_option('display.width', 300) # 设置字符显示宽度
pd.set_option('display.max_rows', None) # 设置显示最大行
pd.set_option('display.max_columns', None)

# print(Nowcoder.loc[(Nowcoder.Language=='C')|(Nowcoder.Language=='CPP'),:]) 
# print(Nowcoder[Nowcoder['Language'].isin (['CPP','C','C#'])])
# print(Nowcoder.query("Language == 'CPP' or Language == 'C'"))
print(Nowcoder.query("Language in ['CPP','C']"))
# print(Nowcoder.loc[Nowcoder.Language.isin(["CPP", "C"])])