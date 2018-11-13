#Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

# For example, given the following Node class

# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# The following test should pass:

# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

from collections import deque

def main():
    test_serialize()
    test_example()
    
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(node):
    if node is None:
        return None
    q = deque()
    q.append(node)
    tree = []
    while(q):
        current = q.popleft()
        if current is not None:
        	tree.append(current.val)
        	q.append(current.left)
        	q.append(current.right)
    result = f"[{','.join(tree)}]"
    return result
    
def deserialize(s):
    values = s[1:-1].split(',')
    nodes = list(map(lambda val: Node(val), values))
    for i,n in enumerate(nodes):
        leftIndex = 2*i+1
        rightIndex = 2*i+2
        n.left = nodes[leftIndex] if leftIndex < len(nodes) else None
        n.right =  nodes[rightIndex] if rightIndex < len(nodes) else None
    return nodes[0]

def test_example():
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    deserialize(serialize(node))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
    
def test_serialize():
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    result = serialize(node)
    assert result == "[root,left,right,left.left]"
   
main()