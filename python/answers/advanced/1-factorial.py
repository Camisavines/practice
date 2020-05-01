# to get a factorial, you must use recursive loops
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * (factorial(x-1))




# BONUS
def generate_fibanocci():
    count = int(input("How many fibonacci numbers would you like to generate? "))
    i = 1
    if count == 0:
        fib = []
    elif count == 1:
        fib = [1]
    elif count == 2:
        fib = [1,1]
    elif count > 2:
        fib = [1,1]
        while i < (count - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1

    return fib