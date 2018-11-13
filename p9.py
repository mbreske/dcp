# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

# Follow-up: Can you do this in O(N) time and constant space?

def main():
  test_example()
  test_example2()
  test_example3()
  test_example4()


def find_largest_sum(arr):
  return max(largest_sum(arr), largest_sum(arr[1:]))

def largest_sum(arr):
  if len(arr) == 1:
    return arr[0] if arr[0] > 0 else 0
  if len(arr) == 2:
    max_val = max(arr)
    return max_val if max_val > 0 else 0
  for i,n in enumerate(arr):
    if i < len(arr) - 2:
      return n + largest_sum(arr[i+2:])
  

def test_example():
  arr = [5,1,1,5]
  sum = find_largest_sum(arr)
  print(sum)
  assert sum == 10

def test_example2():
  arr = [2, 4, 6, 2, 5]
  sum = find_largest_sum(arr)
  print(sum)
  assert sum == 13

def test_example3():
  arr = [-1, 5, -1, 6, -1]
  sum = find_largest_sum(arr)
  print(sum)
  assert sum == 11

def test_example4():
  arr = [-1, -10, -1, 6, -1]
  sum = find_largest_sum(arr)
  print(sum)
  assert sum == -2

main()