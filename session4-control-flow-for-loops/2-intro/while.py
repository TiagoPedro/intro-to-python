import time

count = 0

while count < 3:
    print("Count is:", count)
    # count = count + 1  # Don't forget to update your condition!
    
print(count)

response = ""

response = someAPSAPICall()
# API CALL to APS
while (response == ""):
  time.sleep(10)
  
# do something with the APS API call response