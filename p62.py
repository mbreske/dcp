# There is an N by M matrix of zeroes. Given N and M, write a function to count
# the number of ways of starting at the top-left corner and getting to the bottom-right corner.
# You can only move right or down.

# For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:

# Right, then down
# Down, then right
# Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.

from collections import deque,defaultdict

def main():
  print(pathCount(100,100))

def pathCount(n,m):
  cache = defaultdict(int)
  for i in range(n):
    for j in range(m):
        if i==0 and j==0:
          cache[(i,j)] = 1
        else:
          cache[(i,j)] = cache[(i-1,j)] + cache[(i,j-1)]
  return cache[(n-1,m-1)]

main()