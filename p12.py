# There's a staircase with N steps, and you can climb 1 or 2 steps at a time. 
# Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

# For example, if N is 4, then there are 5 unique ways:

# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2
# What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X?
# For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time. Generalize your function to take in X.

def main():
  test_uniqueWaysToClimb_example()
  test_uniqueWaysToClimb_example2()

#depth = n/min(steps)
#time O(stepCount ^ depth)
#space O(stepCount ^ depth)
def uniqueWaysToClimb(steps, n):
  pathCount = 0
  q = []
  q.append(0)
  while(len(q) > 0):
    stepsTaken = q.pop()
    for s in steps:
      nextStep = stepsTaken + s
      if(nextStep < n):
        q.append(nextStep)
      if(nextStep == n):
        pathCount += 1
  return pathCount

def test_uniqueWaysToClimb_example():
  steps = [1,2]
  n = 4
  assert(uniqueWaysToClimb(steps, n) == 5)

def test_uniqueWaysToClimb_example2():
  steps = [1,3,5]
  n = 4
  assert(uniqueWaysToClimb(steps, n) == 3)

main()