# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

# Given the root to a binary tree, count the number of unival subtrees.

# For example, the following tree has 5 unival subtrees:

#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1

def main():
  num_unival_subtrees(root)

#O(n^2) bad - drill through all subtrees at every step
# def numUnivalTrees(root):
#   if(root is None):
#     return 0
#   left = numUnivalTrees(root.left)
#   right = numUnivalTrees(root.right)
#   return 1 + left + right if isUnival(root) else left + right

# def isUnival(root):
#   return isSubUnival(root, root.value)

# def isSubUnival(root, value):
#   if root.right is None and root.left is None:
#     return True
#   if root.right.val == value and root.left.val == value:
#     return isUnivalTree(root.right.val, value) and isUnivalTree(root.left, value)
#   return False

#O(n) - start at the leaves and percolate up 
def num_unival_subtrees(root):
 count, _ = is_sub_unival(root)
 return count

def is_sub_unival(root):
   if root is None:
    return 0, True
  left_count, is_left_unival = is_left_unival(root)
  right_count, is_left_unival = is_right_unival(root)
  total_count = left_count + right_count
  if is_left_unival and is_right_unival:
    if root.right is not None and root.value != root.right.value
      return total_count, False
    if root.left is not None and root.value != root.left.value
      return total_count, False
    return total_count + 1, True
  return total_count, False

if __name__ == "__main__":
  main()