import pandas as pd
df = pd.read_csv("sales_practice_data_5000.csv",
                 parse_dates=["order_date"],
                 dtype={
                     "product_category" : "category",
                     "region" : "category"
                 })
print(df.info())
print(df.head())

df['customer_rating_calculate'] = df["customer_rating"].map({
    3.3 : "Good",
    4.5 : "Excellent",
    2.9 : "Poor",
    1.1 : "Very Poor"
})
print(df["customer_rating_calculate"].unique())
print(df[["customer_rating","customer_rating_calculate"]].head())
print(df.groupby("customer_rating_calculate").size())

 # applying Map on another Column

df["Payment_Type"] = df["payment_method"].map({
    "Card" : "Digital",
    "Wallet" : "Digital",
    "COD" : "Cash"
})
print(df["Payment_Type"].unique())
print(df[["Payment_Type","payment_method"]].sample(10))

#applying Apply method

def revenue_category(row):
    if row["revenue"] >500:
        return "High"
    elif row["revenue"] >=200:
        return "Medium"
    else:
        return "Low"
df["Revenue_Category"] = df.apply(revenue_category,axis=1)
print(df[["revenue","Revenue_Category"]].sample(10))
print(df.groupby("Revenue_Category").size())

#Applying Pipe method

def add_profit(data):
    data["Profit"] = data["revenue"] * 0.20
    return data
def net_revenue(data):
    data["net_Revenue"] = data["revenue"] - data["Profit"]
    return data 
df = (
    df
    .pipe(add_profit)
    .pipe(net_revenue)
)
print(df)