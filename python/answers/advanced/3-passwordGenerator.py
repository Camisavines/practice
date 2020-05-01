# generate a password with given length
import random

randomchar = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+,./"

passwordLength = int(input("Length of password: >"))
password = ""

for i in range(0, password + 1):
    password += random.choice(randomchar)

print(password)