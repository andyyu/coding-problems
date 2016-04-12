# Andy Yu
'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. 
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree:
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

Difficulty: Medium

Solution notes:
O(n) time
O(n) space
'''

def zigzag_traversal(root):
  stack = [root]  # this will be our working stack
  children = []   # these are are the children of the nodes in the working stack (next level to work on)
  res = []        # result
  level = 0       # keep track of level
  if root == None:    # edge case of empty tree
    return res
  while True:
    for node in stack:
      if node.left != None:
        children.append(node.left)
      if node.right != None:
        children.append(node.right)
    if len(stack) > 0:
      if level % 2: # odd, right to left
        res.append(list(node.val for node in stack[::-1]))  # add the values of all the nodes in the reversed stack
      else: # even, left to right
        res.append(list(node.val for node in stack))        # add the values of all the nodes in the stack
    else:
      break # end of tree
    stack = children   # update the new working stack to be the next level
    children = []      # reset the children stack
    level += 1         # increment the level
  return res