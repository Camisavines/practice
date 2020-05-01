def perfectNumber(x):
    # First step is to get all of its factors, remember to add 1 to the list
    factors = [1]
    for i in range(x, 0, -1):
        if x % 1 == 0:
            factors += [i]

    # Next step, is add all the factors
    sum = 0
    for i in factors:
        sum += i

    # Do the condition
    if ((sum/2) == x):
        return True
    else:
        return False
