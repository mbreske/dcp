# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

def main():
  # input = [1,2,3,4,5]
  # result = buildProductArray(input)
  # print(result)
  buildProductArray_TestExample()
  buildProductArray_TestExample2()
  

#time O(2*n) one pass to build the product and another to build the result
#aux space O(n) to store result
def buildProductArray(input):
  result = []
  product = 1
  for n in input:
    product *= n

  for m in input:
      result.append(int(product/m))
  print(result)
  return result

#Follow-up: what if you can't use division?
#Can use the O(n^2) solution
def buildProductArrayNoDivision(input):
  result = []
  for i,_ in enumerate(input):
    product = 1
    for j,m in enumerate(input):
      if(i!=j):
        product *= m
    result.append(product)





def buildProductArray_TestExample():
  input = [1,2,3,4,5]
  assert(buildProductArray(input) == [120,60,40,30,24])

def buildProductArray_TestExample2():
  input = [3,2,1]
  assert(buildProductArray(input) == [2,3,6])

if(__name__ == "__main__"):
  main()