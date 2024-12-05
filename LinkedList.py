# linear data structure where elements are not stored in contiguous memory locations
# instead, each node contains a reference to the next node in the list

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class LinkedList:
  def __init__(self):
    self.head = None


  def push(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node


  def insertAfter(self, prev_node, new_data):
    if prev_node is None:
      print("given previous node must be in linked list")
      return
    new_node = Node(new_data)
    new_node.next = prev_node.next
    prev_node.next = new_node


  def append(self, new_data):
    new_node = Node(new_data)
    if self.head is None:
      self.head = new_node
      return
    last = self.head 
    while last.next:
      last = last.next
    last.next = new_node

  def printList(self):
    temp = self.head
    while temp:
      print(temp.data, end=" ")
      temp = temp.next

# example usage
llist = LinkedList()
llist.push(10)
llist.push(20)
llish.push(30)

llist.printList()
