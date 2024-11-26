class Stack:
  def __init__(self):
    self.items = []

  def is_empty(self):
    return self.items == []

  def push(self, item):
    self.items.append(item)

  def pop(self):
    if not self.is_empty():
      return self.items.pop()
    else:
      raise IndexError("stack is empty")


  def peek(self):
    if not self.is_empty():
      return self.items[-1]
    else:
      raise IndexError("stack is empty")

  def size(self):
    return len(self.items)

# example usage
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.peek()) # output; 30
print(stack.pop()) #  output; 30
print(stack.pop()) #  output; 30
