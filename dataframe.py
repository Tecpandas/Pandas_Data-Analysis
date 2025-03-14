import pandas as pd
import numpy as np
df = pd.DataFrame({
    "name": [
        "aastha", "atharv", "saury", "anand", "sunita",
        "rohit", "priya", "dev", "kiran", "manoj",
        "ramesh", "sneha", "vijay", "ankita", "raj",
        "meena", "sanjay", "arjun", "neha", "alok",
        "geeta", "nilesh", "varun", "kamal", "pallavi",
        "rahul", "nidhi", "jatin", "swati", "amit",
        "bhavna", "lokesh", "tarun", "simran", "yash",
        "vikas", "kanika", "harsh", "megha", "sumit"
    ],
    "city": [
        "mumbai", "delhi", "indore", "pune", "thane",
        "chennai", "kolkata", "jaipur", "nagpur", "surat",
        "lucknow", "bhopal", "patna", "vadodara", "agra",
        "meerut", "nashik", "kanpur", "ludhiana", "rajkot",
        "ranchi", "howrah", "coimbatore", "jodhpur", "allahabad",
        "gwalior", "vijayawada", "mysore", "bhubaneswar", "salem",
        "warangal", "bareilly", "moradabad", "guntur", "bikaner",
        "noida", "jamshedpur", "bhilai", "cuttack", "firozabad"
    ],
   })
print(df.head(10))
print(type(df))

print(type(df))

# Shape (rows, columns)
print(df.shape)
print(df.iloc[3])
print(df.iloc[:, 0])
print(df.iloc[2, 1]) 
print(df.iloc[0:3, 0:2]) 
print(df.loc[2])  
print(df.loc[2, 'name']) 

print(df.iloc[0:3])  
# Slice by row labels
print(df.loc[1:3])
# First 2 columns
print(df.iloc[:, 0:2])
# Select 'Name' and 'City' columns
print(df.loc[:, ['name', 'city']])


# Add numeric columns for statistical functions
df['name_length'] = df['name'].apply(len)
df['city_length'] = df['city'].apply(len)

# 1. Mean (Average)
print(df[['name_length', 'city_length']].mean())

# 2. Median
print(df[['name_length', 'city_length']].median())

# 3. Mode (Most Frequent Value)
print(df[['name_length', 'city_length']].mode())

# 4. Minimum Value
print(df[['name_length', 'city_length']].min())

# 5. Maximum Value
print(df[['name_length', 'city_length']].max())

# 6. Standard Deviation
print(df[['name_length', 'city_length']].std())

# 7. Variance
print(df[['name_length', 'city_length']].var())

# 8. Count of Non-Null Values
print(df[['name_length', 'city_length']].count())

# 9. Sum of Values
print(df[['name_length', 'city_length']].sum())

# 10. Summary of Statistics
print(df[['name_length', 'city_length']].describe())

