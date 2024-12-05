# data structure where each element has a priority associated with it
# elements are removed from the queue in order of their priority 

import heapq

class PriorityQueue:
  def __init__(self):
    self.heap = []

  def push(self, item, priority):
    heapq.heappush(self.heap, (priority, item))

  def pop(self):
    return heapq.heappop(self.heap)[1]

  def is_empty(self):
    return len(self.heap) == 0

# example usage
pq = PriorityQueue()
pq.push('task1', 3)
pq.push('task2', 1)
pq.push('task3', 5)

while not pq.is_empty():
  print(pq.pop())
