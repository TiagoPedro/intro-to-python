import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Charlie'],
    'Age': [25, 30, 35, None],
    'City': ['New York', 'Los Angeles', 'Chicago', 'New York']
}

df = pd.DataFrame(data)

print("Before:\n", df, "\n")

# Rename columns
# df.rename(columns={"Name": "first_name"}, inplace=True)
# print("After:\n", df, "\n")

# Selecting specific columns
# print("After:\n", df[["Name", "Age"]], "\n")

# Dropping columns
# df.drop(columns=["City"], inplace=True)
# print("After:\n", df, "\n")

# Filtering rows
# print("After:\n", df[df["Age"] > 30], "\n")
# print("After:\n", df[(df["Age"] >= 30) & (df["Name"] == "Bob")], "\n")
