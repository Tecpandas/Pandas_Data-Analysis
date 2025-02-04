




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

# Data Cleaning
# 
df.drop_duplicates(inplace=True)
print(df.head())
#sure the datatype
newset=df["mark"]=df["mark"].astype(int)
print(newset)
newset2=df["age"]=df['age'].astype(int)
print(newset2)
newset3=df['attendance']=df['attendance'].astype(int)
print(newset3)
df["performance_category"] = pd.cut(df["mark"], bins=[0, 50, 75, 100], labels=["Low", "Medium", "High"])
print(df)

#Calculate the mean, median, and standard deviation of marks and attendance.
mean_age=df['mark'].mean()
print(mean_age)
mean_age=df['age'].mean()
print(mean_age)
mean_attendance=df['attendance'].mean()
print(mean_attendance)
#median
median_mark=df['mark'].median()
print(median_mark)
median_age=df['age'].median()
print(median_age)
median_attendance=df['attendance'].median()
print(median_attendance)
#sd
sd_mark=df['mark'].std()
print(sd_mark)
sd_age=df['age'].std()
print(sd_age)
sd_attendance=df['attendance'].std()
print(sd_attendance)
#calculate the lowest and highest marks
low_mark=df['mark'].min()
print(low_mark)
high_marks=df['mark'].max()
print(high_marks)
#students who scored more than 80 marks.
score_mark=df[df['mark']>80]
print(score_mark)
#List students with attendance below 60%.
av_attend=df[df['attendance']<60]
print(av_attend)
#Sort the dataset by marks in asecending order.
descending_order=df['mark'].sort_values()
print(descending_order)
#Find the average mark per city.
avg_mark=df.groupby('city')['mark'].mean()
print(avg_mark)
#Count the number of students in each performance category.
performance_category=df.groupby(["mark", "attendance", "age"])["name"].count()

print(performance_category)

