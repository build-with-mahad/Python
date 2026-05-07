import pandas as pd
Customers = pd.DataFrame({
    "customerID" : [1,2,3],
    "Names" : ["Alice",'Bob',"charlie"]
})
orders = pd.DataFrame({
    "orderID" : [100,101,102,103],
    "customerID" : [1,2,2,3],
    "Amount" : [200,250,750,1000]
})
print(Customers)
print("**************")
print(orders)
print("**************")
Inner_Join = pd.merge(Customers,orders,on='customerID',how='inner')
print("After Inner Join\n",Inner_Join)
print("**************")
left_Join = pd.merge(Customers,orders,on='customerID',how='left')
print('After left Join\n',left_Join)
print("************")
merging = pd.concat([Customers,Customers])
print("After Merging\n",merging)