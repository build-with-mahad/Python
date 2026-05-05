import pandas as pd
series = pd.Series([10,20,20,40,50], index=['a','b','c','d','e'])
print(series)

print(series.values)
print(series.index)
print(series.dtype)

print(series.head)
print(series.tail)
print(series.value_counts())