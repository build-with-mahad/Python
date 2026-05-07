import pandas as pd 
df = pd.read_csv("retail_sales_2.csv",
                 parse_dates=['date'],
                 dtype={
                     'category': 'category',
                     'region' : 'category'
                 })
print(df.head())
df_sorted = df.sort_values(by=['quantity','sales'],ascending=([False,True]))
print("Sorted the Data !..")
print(df_sorted.head())
df['sales_rank'] = df.groupby('quantity')['sales'].rank(method='dense', ascending=False)
print(df)
