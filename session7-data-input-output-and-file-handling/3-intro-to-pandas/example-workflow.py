import pandas as pd

df = pd.read_csv("./session7-data-input-output-and-file-handling/assets/example.csv")

print("Before:\n", df, "\n")
print("head:\n", df.head(), "\n")
print("shape:\n", df.shape, "\n")
print("columns:\n", df.columns, "\n")
print("dtypes:\n", df.dtypes, "\n")
print("describe:\n", df.describe(), "\n")

df.rename(columns={"Name": "Element"}, inplace=True)
# This gives the same result as the line below
# df = df.rename(columns={"Name": "Element"})

df.drop(columns=["Especialidade"], inplace=True)

# Filter to show only elements with volume greater than 5
df_large_elements = df[df["Volume"] > 5]
print(df_large_elements)