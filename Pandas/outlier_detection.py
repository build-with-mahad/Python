import pandas as pd
from scipy.stats import zscore
df = pd.read_csv("sales_practice_data_5000.csv",
                 parse_dates=["order_date"],
                 dtype={
                     "product_category" : "category",
                     "region" : 'category'
                 })
print(df.head(10))
Q1 = df["revenue"].quantile(0.25)
Q3 = df["revenue"].quantile(0.75)
IQR = Q3 - Q1
print(IQR)

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
#identifing outliers
outlier_res = df[(df['revenue']< lower_bound) | (df["revenue"]>upper_bound)]
print(outlier_res.shape)
print(outlier_res[["revenue","product_category"]].head())
#removal outliers
df = df[(df["revenue"] >= lower_bound ) & (df['revenue'] <= upper_bound) ]
print(df.shape)

#zscore Method
df = pd.read_csv("sales_practice_data_5000.csv",
                 parse_dates=["order_date"],
                 dtype={
                     "product_category" : "category",
                     "region" : "category"
                 })
print(df.info())
#Idntifing outliers
df["revenue_z"] = zscore(df["revenue"])
outliers_z = df[(df["revenue_z"].abs() > 3 )]
print(outliers_z.shape)
#removal outliers
df = df[(df["revenue_z"].abs() <=3)]
print(df.shape)

