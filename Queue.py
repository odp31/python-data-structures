class Queue:
  def __init__(self):
    self.queue = []

  def is_empty(self):
    return len(self.queue) == 0

  def enqueue(self, item):
    self.queue.append(item)

  def dequeue(self):
    if not self.is_empty():
      return self.queue.pop(0)
    else:
      raise IndexError("Queue is empty")


  def peek(self):
    if not self.is_empty():
      return self.queue[0]
    else:
      raise IndexError("Queue is empty")

  def size(self):
    return len(self.queue)

# example usage
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue.peek())    # output; 10 
print(queue.dequeue()) # output; 10
print(queue.dequeue()) # output; 20 
