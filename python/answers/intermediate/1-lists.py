# 1
def listSum(xlist):
  sum = 0
  for i in xlist:
    sum += i

  return sum
  
  
# 2
def listMultiply(xlist):
  product = 1
  for i in xlist:
    product *= i

  return product
  
  
# 3
def uniqueItems(xlist):
  result = []
  for i in xlist:
    if i not in result:
      result += [i]
  
  return result
  
  
# 4
def even(xlist):
  result = []
  for i in xlist:
    if i % 2 == 0:
      result += [i]

  return result
  
  