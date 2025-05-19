import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Charlie'],
    'Age': [25, 30, 35, None]
}

df = pd.DataFrame(data)

print(df.isnull().sum())
print(df["Name"].unique())
print(df["Name"].value_counts())