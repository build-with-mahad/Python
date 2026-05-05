import pandas as pd
data = {
    "Name" : ["Alice","Bob",'Charlie',"David"],
    "Age" : [20,25,35,55],
    "City" : ['New York',"Paris","London","France"],
    "Salary" : [20000,30000,50000,71000]
}
df = pd.DataFrame(data)
print(df)
print("**************")
#with loc selection in loc selection last Index is include not exclude
subset_loc = df.loc[0:2,['Name',"Salary"]]
print(subset_loc)
print("**************")
#with iloc selection in iloc selection last index is exclude not include
subset_iloc = df.iloc[0:3,1:3]
print(subset_iloc)
print("**************")
#boolean filtering
high_salary = df[df["Salary"] > 30000]
print(high_salary)
df.loc[df["Age"] > 30 , ["Salary"]] = 85000
print("Low Age Salary Change\n",df.loc[df["Age"] > 30 , ["Salary"]])
