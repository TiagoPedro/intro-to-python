count = 0

def increment():
    count += 1  # ❌ Error: Python thinks this is a local "count", but it wasn't defined

increment()





# count = 0

# def increment():
#     global count
#     count += 1

# increment()
# print(count)  # Output: 1