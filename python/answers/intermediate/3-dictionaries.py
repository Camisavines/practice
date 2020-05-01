bank = {"pennies": 134, "dimes": 4, "nickles": 5, "halfDollar": 2}

# 1
bank["quarters"] = 5

# 2
bank["pennies"] += 14

# 3
bank["halfDollar"] -= 1


# 4
def caseCount(xstring):
    letters = {}
    for i in xstring:
        if letters[i]:
            letters[i] += 1
        else:
            letters[1] = 1
    
    return letters
        