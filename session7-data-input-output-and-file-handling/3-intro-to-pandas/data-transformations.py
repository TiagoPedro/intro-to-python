import pandas as pd

df = pd.read_csv("./session7-data-input-output-and-file-handling/assets/example.csv")

print("Before:\n", df, "\n")

# dropna
# df.dropna(subset=["Area", "Volume"], inplace=True)
# print("After:\n", df)

# notna
# print("notna result:\n", df["Especialidade"].notna(), "\n")
# print("After:\n", df[df["Especialidade"].notna()], "\n")

# sort_values
# df_sorted = df.sort_values("Area", ascending=False)
# print("After:\n", df_sorted, "\n")

# groupby
# print("After:\n", df.groupby("Family")["Volume"].sum(), "\n")
print("After:\n", df.groupby("Family").agg({"Volume": "sum", "Area": "mean"}), "\n")

