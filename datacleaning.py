import pandas as pd
df=pd.read_csv('df.csv')
newdf=df.dropna()
print(newdf)

print(newdf.to_string())
#to drop all wrong data or null data
df1=df.dropna(inplace=True)
print(df1)
#to replace the empty value with fillno func
df2=df.fillna(30,inplace=True)
print(df2)
#to cleaning duplicate data
print(df.drop_duplicates())