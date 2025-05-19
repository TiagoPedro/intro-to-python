import pandas as pd

df = pd.read_excel("./session7-data-input-output-and-file-handling/assets/MapaQuant2_dirty.xlsx")

print("Total rows:", len(df))
missing_volume = df["Volume"].isnull().sum()
print("Rows with missing volume:", missing_volume)
print(df[df["Volume"].isnull()])