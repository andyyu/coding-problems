# Andy Yu
'''
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

Difficult: Easy

Solution Notes:

O(n) time
O(1) space
'''
def is_same_tree(p, q):
  if not p and not q:
    return True
  elif p and q and p.val == q.val:
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
  else:
    return False