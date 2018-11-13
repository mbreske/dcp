def main():
  nums = [10, 15, 3, 7, -10]
  k = -3
  result = doTwoElementsSumToK(nums, k)
  print(result)
  test_negative_case()
  test_positive_case()


#Time: O(n) - n constant time insertions and lookups in hash table
#Add Space: O(n) - store n complements in hash table
def doTwoElementsSumToK(numbers, k):  
  complements = {}
  for n in numbers:
    if(n in complements):
      return True
    complements[k-n] = True
  return False

#Scaling
#Two pass approach
#Divide input across machines
#Pass #1: populate the shared complement table - coordinate "done"
#Pass #2: listen for "done" then check local number list against complements - broadcast result

#Tests
def test_positive_case():
  nums = [10, 15, 3, 7]
  k = 17
  assert(doTwoElementsSumToK(nums, k) == True)

def test_negative_case():
  nums = [10, 15, 3, 7]
  k = 99
  assert(doTwoElementsSumToK(nums, k) == False)

if __name__ == "__main__":
  main()