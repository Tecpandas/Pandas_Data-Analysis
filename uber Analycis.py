import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("C:\\Users\\astha\\Downloads\\UberDataset.csv")


print(df.info)
print(df.describe)
#filling missing value
print(df.mean)
print(df.median)
#REMOVE NULL VALUE
df.isnull().sum()
print(df)
print(df.fillna('N'))
#by forward fill
df.fillna(method='ffill', inplace=True)
print(df)
#backward fill
df.fillna(method='bfill',inplace=True)
print(df)
#duplicate value
df.duplicated()
print(df)
df_cleaned = df.drop_duplicates(keep='first')
print(df_cleaned)
df_cleaned1 = df.drop_duplicates(keep='last')
print(df_cleaned1)
#convert the dat into datetime
# Convert START_DATE and END_DATE to datetime format
df['START_DATE'] = pd.to_datetime(df['START_DATE'], errors='coerce')
df['END_DATE'] = pd.to_datetime(df['END_DATE'], errors='coerce')

#