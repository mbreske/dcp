#Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

from datetime import datetime, timedelta
import threading
import uuid
import queue
from heapq import heappush, heappop

def main():
  s = Scheduler()
  t = threading.Thread(target=s.run)
  t.start()
  s.insert(lambda : print('hello world'), 2000)
  s.insert(lambda : print('hello world'), 3000)
  s.insert(lambda : print('hello world'), 4000)

class Scheduler():
  def __init__(self):
    self.heap = []

  def getMin(self):
    return self.heap[0] if len(self.heap) else None

  def insert(self, f, n):
    promised = datetime.utcnow() + timedelta(milliseconds=n)
    heappush(self.heap, (promised,f))

  def removeMin(self):
    return heappop(self.heap)

  def run(self):
    while(1):
      nextJob = self.getMin()
      if nextJob is None:
        continue
      if(nextJob[0] <= datetime.utcnow()):
        job = self.removeMin()
        job[1]()

main()