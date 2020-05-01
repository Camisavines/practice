def add(x,y):
    return x + y
  
def sub(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return x ** y

def modulus(x, y):
    return x % y

def integer_division(x, y):
    return x // y



######################## TESTS ########################

print(add(2,3)) # 5
print(add("2","3")) # 23
print(sub(10,3)) # 7
print(sub(5,7)) # -2
print(multiply(4,3)) # 12
print(multiply("a",3)) # aaa
print(divide(12,3)) # 4.0
print(divide(24,3)) # 8.0
print(power(2, 3)) # 8
print(power(1, 5)) # 1
print(modulus(10, 2)) # 0
print(modulus(10, 3)) # 1
print(integer_division(10,3)) # 3
print(integer_division(7, 3)) # 2