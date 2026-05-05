import pandas as pd
import openpyxl
df =  pd.read_csv("retail_sales.csv",
                  parse_dates=["date"],
                  dtype={
                      "category" : "category",
                      "region" : "category"
                  })
df.info()
clean_df = df[df["sales"] > 0]
subset = clean_df[["date",'category','quantity','profit']]

subset.info()

subset.to_excel("subset_sales.xlsx",sheet_name="sales")
subset.to_json("subset_sales.json",orient="records",date_format="iso")
print("File Exported!....")
subset.info()