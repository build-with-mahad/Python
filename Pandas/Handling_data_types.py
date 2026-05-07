import pandas as pd
df = pd.read_csv("retail_sales.csv",
                 parse_dates=["date"],
                 dtype={
                     "category" : "category",
                     "region" : 'category'
                 })
df.info()

df["quantity"] = pd.to_numeric(df["quantity"])
df.info()
df['region'] = df["region"].astype('category')
print(df["region"])