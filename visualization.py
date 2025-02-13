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
    #randint genertate the random some number to some number with some size
   "mark": np.random.randint(30, 100, size=40),
    "age": np.random.randint(18, 30, size=40),
    "attendance": np.random.randint(50, 100, size=40)
})

import matplotlib.pyplot as plt
import seaborn as sns

#Box plot of marks to analyze outliers.
x=df['mark']
plt.boxplot(x)
plt.show()

#Heatmap to show correlation between marks, attendance, and age.
corr_matrix=df.corr()
plt.figure(figsize=(6,4))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.show()

