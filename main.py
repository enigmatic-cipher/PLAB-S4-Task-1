"""
Task (1.1): Create a function named isMultipleOf3 that takes an integer n as input and print whether n is a multiple of 3 or not.
Task (1.2): Given an integer list as input. Use isMultipleOf3 function from Task 1.1 to print Yes/No for each element in the list. [21,4,12,32,33]
"""

def isMultipleof3(n):
  if n%3==0:
    return "Yes"
  else:
    return "No"

ls = [21,4,12,32,33]
ln = len(ls)
for i in range(0,ln):
  e = ls[i]
  print(f"{e}: {isMultipleof3(e)}")
  