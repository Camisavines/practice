# 1
def reverseString(xstring):
  result = ""
  for i in xstring:
    result = i + result

  return result
  
  
# 2
def letterCount(xstring):
  counter = {}
  for i in xstring:
    if i in counter:
    counter[i] += 1
    else:
    counter[i] = 1

  return counter


# 3
def palindrome(xstring):
  reversed = ""
  for i in xstring:
    reversed = i + reversed
  if (xstring == reversed):
    return True
  else:
    return False



# 4
def isogram(xstring):
  wordList = []
  for i in xstring:
    if i in wordList:
      return False
    else:
      wordList += [i]
  return True

