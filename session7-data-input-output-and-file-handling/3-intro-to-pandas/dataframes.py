import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
}

df = pd.DataFrame(data)
print(df)



# df.head()         # First 5 rows
# df.tail()         # Last 5 rows
# df.shape          # (rows, columns)
# df.columns        # List of column names
# df['Age'].mean()  # Average age