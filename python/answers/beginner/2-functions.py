def minTwo(x, y):
    if x < y:
      return x
    else:
      return y
  
  
def maxTwo(x, y):
    if x < y:
        return y
    else:
        return x


def minThree(x, y, z):
    if (x < y) and (x < z):
        return x
    elif (y < x) and (y < z):
        return y
    elif (z < x) and (z < y):
        return z
    elif (z == y) and (z == x):
        return ("All values are the same: " + z)
    elif (z < x) and (z == y):
        return ("Values 2 and 3 are the same: " + z)
    elif (z > x) and (x == y):
        return ("Values 1 and 2 are the same: " + x)
    else:
        return ("Values 1 and 3 are the same: " + x)

      
  
def maxThree(x, y, z):
    if (x > y) and (x > z):
        return x
    elif (y > x) and (y > z):
        return y
    elif (z > x) and (z > y):
        return z
    elif (z == y) and (z == x):
        return ("All values are the same: " + z)
    elif (z > x) and (z == y):
        return ("Values 2 and 3 are the same: " + z)
    elif (x > z) and (x == y):
        return ("Values 1 and 2 are the same: " + x)
    else:
        return ("Values 1 and 3 are the same: " + x)
  
  
  
######################## TESTS ########################
print("Min of Two")
x = input("Value 1: ")
y = input("Value 2: ")
print(minTwo(x, y))

print("\nMax of Two")
x = input("Value 1: ")
y = input("Value 2: ")
print(maxTwo(x, y))

print("\nMin of Three")
x = input("Value 1: ")
y = input("Value 2: ")
z = input("Value 3: ")
print(minThree(x, y, z))

print("\nMax of Three")
x = input("Value 1: ")
y = input("Value 2: ")
z = input("Value 3: ")
print(maxThree(x, y, z))

  