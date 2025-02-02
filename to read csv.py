import pandas as pd
df=pd.read_csv("df.csv")
print(df.to_string())
#to count max row

print(pd.options.display.max_rows) 
# to read top five dataset
print(df.head())
print(df.tail())
print(df.info())#to get more info
print(df.loc[[0, 1,2,3,4]])