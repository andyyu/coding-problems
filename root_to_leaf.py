# Andy Yu
'''
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.

Difficulty: Medium

Solution notes:

The algorithm does a breadth-first traversal of the tree, updating each node to have the cumulative sum of the nodes before it.
If the node has no children (it's a leaf), we add it to the final return value.

O(n) time 
O(1) space
'''

def sumNumbers(self, root):
  if not root:
    return 0
  ret = 0
  stack = [root]
  for node in stack:
    if node.left:
      node.left.val = 10*node.val + node.left.val
      stack.append(node.left)
    if node.right:
      node.right.val = 10*node.val + node.right.val
      stack.append(node.right)
    if not (node.left or node.right):
      ret += node.val
  return ret
