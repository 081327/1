import pandas as pd
signup = pd.read_csv('signup.csv')
items = pd.read_csv('items.csv')
df = pd.merge(items,signup,how='left',on='item_id')
df = df.groupby('item_name').employee_id.count()
print(df)
