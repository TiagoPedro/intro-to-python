# Division by zero
x = 10
y = 0
# print(x / y) # This will raise a ZeroDivisionError

# Confusing % with //
print("Remainder:", 10 % 3)   # 1 → remainder
print("Integer part:", 10 // 3)  # 3 → integer part

# Operator precedence matters:
print("5 + 3 * 2 =", 5 + 3 * 2)   # 11, not 16
print("(5 + 3) * 2 =", (5 + 3) * 2) # 16
