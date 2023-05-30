import pandas as pd
signup = pd.read_csv('signup.csv')
signup1 = pd.read_csv('signup1.csv')
items = pd.read_csv('items.csv')
signup_pro = signup.merge(signup1,how='outer')
new = items.merge(signup_pro,on='item_id',how='left')
print(new.groupby('item_name')['employee_id'].count())