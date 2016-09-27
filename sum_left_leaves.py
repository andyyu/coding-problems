# Andy Yu
'''
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

Difficult: Easy

Solution Notes:
Do this recursively, DFS. If it's a left leaf, return value.


'''
def sum_of_left_leaves(self, root, left=False):
  if root:
    if not root.left and not root.right and left:
      return root.val
    else:
      return self.sumOfLeftLeaves(root.left, True) + self.sumOfLeftLeaves(root.right)
  else:
    return 0