import pandas as pd
data = {
    "Name" : ["Alice","Bob",'Charlie'],
    "Age" : [20,30,40],
    "City" : ['London','Paris','United Kingdom']
}
df = pd.DataFrame(data)
print(df)

df = pd.read_csv("retail_sales.csv")
print("Info:\n",df.info())
print("****************")
print("Shape:\n",df.shape,df.dtypes)
print("****************")
print("Statisticsl Info\n",df.describe())