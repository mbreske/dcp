# Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

# For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

# In this example, assume nodes with the same value are the exact same node objects.

# Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.

def main():
  A = [3,7,8,10]
  B = [2,11,99,1,8,10]
  print(getIntersectingNode(A,B))

def getIntersectingNode(a, b):
  lenA = len(a)
  lenB = len(b)
  if lenA > lenB:
    longList = a
    shortList = b
  else:
    longList = b
    shortList = a
  
  diff = lenA - lenB
  for j in range(len(shortList)):
    if longList[j+diff] == shortList[j]:
      return shortList[j]

  
main()