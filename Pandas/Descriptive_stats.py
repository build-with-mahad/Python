import pandas as pd 
df = pd.read_csv("sales_practice_data_5000.csv",
                 parse_dates=["order_date"],
                 dtype={
                     "product_category" : "category",
                     "region" : "category"
                 })
print(df.info())
print(df.shape)
print(df.dtypes)

print(df[["unit_price","revenue"]].describe())
print(df["revenue"].mean())
print(df["revenue"].median())
print(df["revenue"].skew())
print(df["revenue"].quantile([0.25,0.50,0.75]))
print(df.groupby("product_category")["revenue"].describe())
print(df.groupby("product_category")["revenue"].mean())

Q1 = df["revenue"].quantile(0.25)
Q3 = df["revenue"].quantile(0.75)
IQR = Q3 - Q1

print(IQR)
print(Q3 > Q1 and IQR > 0)
