def maxTwoSum(x, y, z):
    if (x < y) and (x < z):
      return (y + z)
    elif (y < x) and (y < z):
      return (x + z)
    elif (z < x) and (z < y):
      return (x + y)
    elif (z == x) and (z == y):
      return (z + x)
    elif (z < x) and (x == y):
      return (x + y)
    elif (x < z) and (z == y):
      return (y + z)
    elif (y < x) and (x == z):
      return (x + z)
    else:
      return
  
  
  
def minTwoSum(x, y, z):
    if (x > y) and (x > z):
      return (y + z)
    elif (y > x) and (y > z):
      return (x + z)
    elif (z > x) and (z > y):
      return (x + y)
    elif (z == x) and (z == y):
      return (z + x)
    elif (z > x) and (x == y):
      return (x + y)
    elif (x > z) and (z == y):
      return (y + z)
    elif (y > x) and (x == z):
      return (x + z)
    else:
      return
  
  
  
  
  

######################## TESTS ########################

# JUST ALLOW THE USER TO INPUT THE VALUES
X = input("value 1: ")
Y = input("value 2: ")
Z = input("value 3: ")

print("Max Sum Two")
print(maxTwoSum(X, Y, Z))

print("\nMin Sum Two")
print(minTwoSum(X, Y, Z))