import pandas as pd
df =  pd.read_csv("sales_practice_data_5000.csv",
                  parse_dates=["order_date"],
                  dtype={
                      "product_category" : "category",
                      "region" : "category"
                  })
print(df.head())
df = df.set_index("order_date")
print(df.index)

monthly_revenue = df["revenue"].resample("ME").sum()
print(monthly_revenue)

print(monthly_revenue.pct_change())
print(monthly_revenue.index.is_monotonic_increasing)

print(monthly_revenue.sum(),df["revenue"].sum())
print(monthly_revenue.sum() <= df["revenue"].sum())