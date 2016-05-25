# Andy Yu
'''
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9

to

     4
   /   \
  7     2
 / \   / \
9   6 3   1

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

Difficulty: Easy

Solution notes:

My first iteration looked something like this -
def invert_tree(root):
  if not root:
    return None
  else:
    temp_left = root.left
    root.left = invert_tree(root.right)
    root.right = invert_tree(temp_left)
  return root

After some optimization, we end up with a concise 3 line solution!
Note: if we are seeking optimal performance over code brevity, then we should add more "checks".

if not root:
  return None

should always be checked for each node.
also check things like

if not root.left and not root.right:
  return root

if root.right / root.left:
  root.left/right = invert_tree(root.right)

This way our code will only attempt to call invert_tree when possible / needed.
This will increase performance (not by much, but if you're really trying to squeeze every bit of speed)

O(n) time 
O(1) space

'''
def invert_tree(root):
  if root:
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
  return root