import pandas as pd

df = pd.read_excel("./session7-data-input-output-and-file-handling/assets/MapaQuant2_dirty.xlsx")
df = df[df["Especialidade"].notna()]
df["Type"] = df["Type"].replace("", "Unknown")

df["Total_Solid_Mass"] = df["Volume"] * 2.5

summary = df.groupby("Family").agg({
    "Volume": "sum",
    "Area": "mean",
    "Total_Solid_Mass": "sum"
}).sort_values(by="Total_Solid_Mass", ascending=False)

print(summary)
