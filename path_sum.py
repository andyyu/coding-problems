# Andy Yu
'''
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

Difficulty: Easy - Medium

Solution notes:
O(n) time
O(1) space

This initial recursive solution is much cleaner, but it fails for the edge case of an empty tree and a sum of 0
which should return false, but returns true in this implementation.

def has_path_sum(root, sum):
  if root == None:
    return sum == 0
  else:
    return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)

So we must edit our implementation to account for this.

recursion
'''

def has_path_sum(root, sum):
  if root == None:
    return False
  if root.left == None and root.right == None:
    return sum == root.val
  else:
    return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)
