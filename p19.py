# A builder is looking to build a row of N houses that can be of K different colors.
# He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

# Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color,
# return the minimum cost which achieves this goal.


# 7 8 9
# 2 5 1
# 4 9 7
from math import inf

def main():
  input = [[1,2,3], [4,5,6], [7,8,9]]
  print(minBuildCost(input))

def minBuildCost(houseCosts):
  min_cost = 0
  min_cost_index = -1
  second_min_cost = 0

  for _,row in enumerate(houseCosts):
    new_min_cost,new_min_cost_index = inf, -1
    new_second_min_cost = inf
    for j,price in enumerate(row):
      prev_min_cost = second_min_cost if j == min_cost_index else min_cost
      cost = prev_min_cost + price
      if cost < new_min_cost:
        new_second_min_cost = new_min_cost
        new_min_cost, new_min_cost_index = cost, j
      elif cost < new_second_min_cost:
        new_second_min_cost = cost
    min_cost = new_min_cost
    min_cost_index = new_min_cost_index
    second_min_cost = new_second_min_cost
  return min_cost

main()