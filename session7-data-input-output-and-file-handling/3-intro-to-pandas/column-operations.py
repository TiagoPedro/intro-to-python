import pandas as pd

df = pd.read_csv("./session7-data-input-output-and-file-handling/assets/example.csv")

print("Before:\n", df, "\n")

# Calculate volume cost at 75€/m³
df["Concrete_Cost"] = df["Volume"] * 75
print("After:\n", df, "\n")

# Add base and top slab thicknesses
# df["Total_Thickness"] = df["Base_Thickness"] + df["Top_Thickness"]
# print("After:\n", df, "\n")

# Convert Area from m² to ft² (1 m² = 10.7639 ft²)
# df["Area_ft2"] = df["Area"] * 10.7639
# print("After:\n", df, "\n")