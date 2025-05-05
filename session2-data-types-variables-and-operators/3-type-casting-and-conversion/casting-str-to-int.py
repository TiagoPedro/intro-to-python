# Explicit casting example
num_str = "100"
num_int = int(num_str)
print("Converted Number:", num_int)
print("Type of num_str:", type(num_str))
print("Type of num_int:", type(num_int))

# Potential error:
# Uncomment the next line to see what happens:
print(int("101"))