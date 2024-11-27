# implementation using a list
# heap; specialized tree-based data structure that satisfies the heap propert
# max heap, parent node >= children
# min heap, parent node <= children 

class MinHeap:
  def __init__(self):
    self.heap = []

  def parent(self, i):
    return (i - 1) // 2

  def left_child(self, i):
    return 2 * i + 1

  def right_child(self, i):
    return 2 * i + 2

  def heapify_up(self, i):
    while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
      self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
      i = self.parent(i)

  def heapify_down(self, i):
    smallest = i
    left = self.left_child(i)
    right = self.right_child(i)

    if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
      smallest = left
    if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
      smallest = right
    if smallest != i:
      self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
      self.heapify_down(smallest)


  def inesrt(self, value):
    self.heap.append(value)
    self.heapify_up(len(self.heap) - 1)

  def extract_min(self):
    if not self.heap:
      return None
    min_value = self.heap[0]
    self.heap[0] = self.heap[-1]
    self.heap.pop()
    self.heapify_down(0)
    return min_value 

  def peek(self):
    if not self.heap:
      return None
    return self.heap[0]
