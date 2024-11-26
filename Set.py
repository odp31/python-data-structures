class MySet:
  def __init__(self):
    self.elements = []

  def add(self, element):
    if element not in self.elemetns:
      self.elements.append(element)

  def remove(self, element):
    if element in self.elements:
      self.elements.remove(element)


  def contains(self, element):
    return element in self.elements

  def union(self, other_set):
    result = MySet()
    result.elements = self.elements + other_set.elements
    return result 

  def intersection(self, other_set):
    result = MySet()
    for element in self.elements:
      if element in other_set.elements:
        result.add(element)
    return result


  def difference(self, other_set):
    result = MySet()
    for element in self.elements:
      if element not in other_set.elements:
        result.add(element)
    return result 

  def is_subset(self, other_set):
    for element in self.elements:
      if element not in other_set.elements:
        return False
    return True 

def __str__(self):
  return str(self.elements)

# example usage
set1 = MySet()
set1.add(1)
set1.add(2)
set1.add(3)

set2 = MySet()
set2.add(2)
set2.add(3)
set2.add(4)

print("set 1; ", set1)
print("set 2; ", set2)

print("union; ", set1.union(set2))
print("intersection: ", set1.intersection(set2))
print("difference (set1 - set2):", set1.difference(set2))
print("is set1 a subset of set2?", set1.is_subset(set2))
