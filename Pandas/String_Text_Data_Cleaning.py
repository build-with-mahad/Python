import pandas as pd
df = pd.DataFrame({
    "Category" : [' Electronics','furniture','Home-appliances','elecTrOnics','   Furniture   ']
})
print(df)
df['Category_clean'] = df['Category'].str.strip().str.lower()
# print(df)
df["Category_clean"] = df['Category_clean'].str.replace('-',' ')
print(df)