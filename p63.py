# Given a 2D matrix of characters and a target word, write a function that returns
# whether the word can be found in the matrix by going left-to-right, or up-to-down.

# For example, given the following matrix:

# [['F', 'A', 'C', 'I'],
#  ['O', 'B', 'Q', 'P'],
#  ['A', 'N', 'O', 'B'],
#  ['M', 'A', 'S', 'S']]
# and the target word 'FOAM', you should return true, since it's the leftmost column.
# Similarly, given the target word 'MASS', you should return true, since it's the last row.

#Time: O(M*N) * 4*(len(word)-1)
#Space: O(1) auxillary
def main():
  input = [['F', 'A', 'C', 'I'],
          ['O', 'B', 'Q', 'P'],
          ['A', 'N', 'O', 'B'],
          ['M', 'A', 'S', 'S']]
  print(containsWord('BONA', input))

def containsWord(word, chars):
  for i in range(len(chars)):
    for j in range(len(chars[0])):
      if (checkWordUp(i,j,word,chars) or
          checkWordDown(i,j,word,chars) or
          checkWordRight(i,j,word,chars) or
          checkWordLeft(i,j,word,chars)):
          return True
  return False

def checkWordUp(i,j,word,chars):
  if len(word) > i + 1:
    return False
  for k in range(len(word)):
    if chars[i-k][j] != word[k]:
      return False
  print('up')
  return True

def checkWordDown(i,j,word,chars):
  if len(word) > len(chars) - i:
    return False
  for k in range(len(word)):
    if chars[i+k][j] != word[k]:
      return False
  print('down')
  return True

def checkWordRight(i,j,word,chars):
  if len(word) > len(chars[0]) - j:
    return False
  for k in range(len(word)):
    if chars[i][j+k] != word[k]:
      return False
  print('right')
  return True

def checkWordLeft(i,j,word,chars):
  if len(word) > j + 1:
    return False
  for k in range(len(word)):
    if chars[i][j-k] != word[k]:
      return False
  print('left')
  return True

main()