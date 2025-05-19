# 1. Ask for a sentence and manipulate it
sentence = input("Type a sentence: ")
print("Uppercase:", sentence.upper())
print("Length:", len(sentence))
print("Split:", sentence.split(" "))

# 2. List manipulation
fruits = ["banana", "apple", "orange"]
print("Sorted:", sorted(fruits))
print("Joined:", " | ".join(fruits))
print("Reversed:", list(reversed(fruits)))

# Get user input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = sum([num1, num2])
print("Sum:", result)