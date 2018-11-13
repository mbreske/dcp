# Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.

# For example, given the following preorder traversal:

# [a, b, d, e, c, f, g]

# And the following inorder traversal:

# [d, b, e, a, f, c, g]

# You should return the following tree:

#     a
#    / \
#   b   c
#  / \ / \
# d  e f  g

def main():
  preOrder = ["a", "b", "d", "e", "c", "f", "g"]
  inOrder = ["d", "b", "e", "a", "f", "c", "g"]
  root = constructTree(preOrder, inOrder)
  printTree(root)
  print('')
  printTreeInOrder(root)

def constructTree(preOrder, inOrder):
  preIndex = 0
  def buildTree(preOrder, inOrder):
    nonlocal preIndex
    if preIndex >= len(preOrder):
      return None

    rootVal = preOrder[preIndex]
    if rootVal not in inOrder:
      return None

    root = Node(rootVal)
    rootIndex = inOrder.index(rootVal)
    leftSubTree = inOrder[:rootIndex]
    rightSubTree = inOrder[rootIndex+1:]

    preIndex += 1
    root.left = buildTree(preOrder, leftSubTree)
    root.right = buildTree(preOrder, rightSubTree)
    return root

  return buildTree(preOrder,inOrder)

def printTree(root):
  if root:
    print(root.data)
    printTree(root.left)
    printTree(root.right)

def printTreeInOrder(root):
  if root:
    printTreeInOrder(root.left)
    print(root.data)
    printTreeInOrder(root.right)


class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

main()