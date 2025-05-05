cement_in_stock = False
steel_in_stock = False
bricks_in_stock = True

if cement_in_stock and steel_in_stock and bricks_in_stock:
    print("All materials are available.")
elif cement_in_stock or steel_in_stock or bricks_in_stock:
    print("Some materials are available.")
else:
    print("No materials are available.")