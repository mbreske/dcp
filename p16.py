# You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

# record(order_id): adds the order_id to the log
# get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
# You should be as efficient with time and space as possible.

import random

def main():
  log = Log(10)
  ids = [random.randint(0,100) for _ in range(0,10**6)]
  print (ids[-10:])
  for id in ids:
    log.record(id)
  print (log.get_last(6))
  # log = Log(3)
  # log.record('x')
  # log.record('y')
  # log.record('c')
  # log.record('a')
  # log.record('b')
  # print (log.get_last(3))

#circular buffer
class Log():  
  def __init__(self, n):
    self.data = [None for _ in range(0,n)]
    self.n = n
    self.head = -1
  
  #O(1) insert
  #O(n) total space
  def record(self, id):
    #index alternates between 0 and n-1
    self.head = (self.head + 1) % self.n
    self.data[self.head] = id

  #O(1) retrieval
  def get_last(self,i):
    last = (self.head + self.n - i + 1) % self.n
    return self.data[last]

main()