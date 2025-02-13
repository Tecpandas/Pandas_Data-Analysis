import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
df=pd.DataFrame(
    data = {
    "Restaurant Name": [f"Restaurant {i}" for i in range(1, 101)],
    "Cuisine": random.choices(["Indian", "Chinese", "Italian", "Mexican", "Japanese", "Continental", "Fast Food"], k=100),
    "Location": random.choices(["Mumbai", "Delhi", "Bangalore", "Kolkata", "Hyderabad", "Pune", "Chennai"], k=100),
    "Rating": [round(random.uniform(3.0, 5.0), 1) for _ in range(100)],
    "Number of Reviews": [random.randint(500, 1500) for _ in range(100)],
    "Price for Two": [random.randint(300, 2000) for _ in range(100)],
    "Delivery Option": random.choices(["Yes", "No"], k=100),
    "Vegetarian": random.choices(["Yes", "No"], k=100),
    "Discount Available": random.choices(["Yes", "No"], k=100),
    "Opening Hours": random.choices(["10:00 AM - 11:00 PM", "12:00 PM - 10:00 PM", "9:00 AM - 11:00 PM", "1:00 PM - 11:00 PM"], k=100)
}

)
df1=pd.DataFrame(df)
#df2=df.to_csv('zomtoto.csv')
df3=pd.read_csv('zomtoto.csv')
print(df.to_string())
# convert the data type of the “rate” column to float and remove the denominator
conv=df['Rating']=df['Rating'].astype(float)
print(conv)
x=df['Cuisine']
y=df['Restaurant Name']
plt.bar(x,y)
plt.show()

