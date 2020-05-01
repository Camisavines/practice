numbers = [6, 23, 7, 14, 6, 8]
company = "South Bend Code School"
instructors = ["CamisaV", "KristenH", "KennyJ", "PaulM", "JasonZ", "AlexS"]

print(numbers[1]) #23
print(company[11]) #C
print(instructors[4]) #JasonZ

# 3
def getInstructors():
    for i in instructors:
        print(i)

# 4
def getInitials():
    for i in instructors:
        print(i[0] + i[-1])

# 5
def slicing():
    print(numbers[2:4])
    print(company[:15])
    print(instructors[1:])