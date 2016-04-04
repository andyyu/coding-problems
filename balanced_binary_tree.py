# Andy Yu
'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree 
in which the depth of the two subtrees of every node never differ by more than 1.
Difficulty: Easy

Solution notes:

Naive solution: just consider the definition of a balanced binary tree!
def get_depth(root):
  if root == None:
    return 0
  else:
    return max(get_depth(root.left) + get_depth(root.right) + 1

def is_balanced(root):
  if root == None:
    return True
  else:
    return math.abs(get_depth(root.left) - get_depth(root.left)) <= 1 and is_balanced(root.left) and is_balanced(root.right)

However, this solution is slow. Really slow. O(N^2) since we have to access every child node of every node in the tree.
We can do better than that. We don't need to recalculate each depth every time, so we can do a DFS type approach.

O(n) time
O(1) space
'''

def dfs_height(root):
  if root == None:
    return 0
  else:
    left_st = is_balanced(root.left)
    right_st = is_balanced(root.right)
    if math.abs(left_st - right_st) > 1 or left_st == -1 or right_st == -1≥:
      return -1
    else:
      return max(left_st, right_st) + 1

def is_balanced(root):
  return dfs_height(root) != -1
