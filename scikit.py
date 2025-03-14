from sklearn import datasets
import pandas as pd
from sklearn.model_selection import train_test_split

# Load breast cancer dataset
data =datasets.load_breast_cancer()

# Convert to DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

print(df.head())
print(df.info())
x=df.drop('target',axis=1)
y=df['target']

x_train,x_test,y_train,y_test=train_test_split(  x, y, test_size=0.2, stratify=y, random_state=42)
print("Training set size:", x_train.shape)
print("Test set size:", y_test.shape)
