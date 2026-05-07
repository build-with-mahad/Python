import pandas as pd
df = pd.read_csv("retail_sales_2.csv",
                 parse_dates=["date"],
                 dtype={
                     "category" : "category",
                     "region" : "category"
                  })
df.head()
df.info()
print(df.isna().sum())
df['quantity'] = pd.to_numeric(df['quantity'])
df["quantity"] = df["quantity"].fillna(df["quantity"].mode()[0])
print(df.isna().sum())
df['sales'] = df["sales"].fillna(df["sales"].mean())
print(df.isna().sum())
df["category"] = df["category"].fillna(df["category"].mode()[0])
print(df.isna().sum())
df['profit'] = df["profit"].fillna(df["profit"].median())
print(df.isna().sum())
df.dropna(subset=['region'],inplace=True)
print(df.isna().sum())
df.info()