# Given an array of integers, find the first missing positive integer in linear time and constant space.
# In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

# You can modify the input array in-place.

def main():
  testExample1()
  testExample2()
  testDuplicates()

#time O(n)
#aux space O(1)
def firstMissingPositive(input):
  for i,n in enumerate(input):
    while input[i] < len(input) and input[i] > 0:
      if(i == n):
        break
      if(input[i] == input[n]):
        break
      input[i], input[n] = input[n], input[i]
      n = input[i]

  for i,n in enumerate(input):
    if i != n and i > 0:
      return i
  return len(input)

# first attempt - O(3n)
# def firstMissingPositive(input):
#   for n in input:
#     if n < 0:
#       input.remove(n)
#   for i,n in enumerate(input):
#     n = n if n > 0 else -n
#     if(n < len(input)):
#       input[n] = -input[n] if input[n] > 0 else input[n]
#   for i,n in enumerate(input):
#     if n > 0 and i > 0:
#       return i
#   return len(input)

def testExample1():
  input = [3,4,-1,1]
  actual = firstMissingPositive(input)
  expected = 2
  assert actual == expected

def testExample2():
  input = [1,2,0]
  actual = firstMissingPositive(input)
  expected = 3
  assert actual == expected

def testDuplicates():
  input = [3,4,4,-1,1,1]
  actual = firstMissingPositive(input)
  expected = 2
  assert actual == expected

main()