import pandas as pd
new=pd.read_csv(r"C:\Users\astha\Downloads\sales-data-sample.csv")
print(new)
new1=new.head()
print(new1)
print(new.duplicated())