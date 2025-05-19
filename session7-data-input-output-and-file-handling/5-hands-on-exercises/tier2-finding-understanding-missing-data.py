import pandas as pd

df = pd.read_excel("./session7-data-input-output-and-file-handling/assets/MapaQuant2_dirty.xlsx")
df_clean = df.dropna(subset=["Area", "Volume"])

df_filtered = df_clean[(df_clean["Volume"] > 50) & (df_clean["Area"] > 100)]
df_filtered["Area_to_Volume"] = df_filtered["Area"] / df_filtered["Volume"]

sorted_df = df_filtered.sort_values(by="Area_to_Volume", ascending=False)
print(sorted_df)