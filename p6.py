# An XOR linked list is a more memory efficient doubly linked list.
# Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node.
# Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

# If using a language that has no pointers (such as Python), you can assume you have access to get_pointer
# and dereference_pointer functions that converts between nodes and memory addresses.

class LinkedList:
  def __init__(self):
    self.head = None
    self.end = None

  def add(self, element):
    if(self.head is None):
      newNode = Node(element)
      self.head = get_pointer(newNode)
      self.end = self.head
    newNode = Node(element)
    newNodeAddr = get_pointer(newNode)
    prevNode = dereference_pointer(self.end)
    prevNode.both = prevNode.both ^ newNodeAddr
    newNode.both = self.end
    self.end = newNodeAddr

  def get(self, index):
    current = self.head
    prev = 0
    for _ in range(0,index+1):
        nextPrev = current
        current = prev ^ dereference_pointer(current).both
        prev = nextPrev
    return dereference_pointer(current)


def get_pointer(obj):
  return 1

def dereference_pointer(ptr):
  return Node(0)

class Node:
  def __init__(self, data):
    self.data = data
    self.both = 0