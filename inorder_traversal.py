# Andy Yu
'''
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,3,2].

Difficulty: Medium

Solution notes:

Recursive solution:

def inorder_traversal(root):
  if (root == null):
    return
  inorder_traversal(root.left)
  append(root)
  inorder_traversal(root.right)

But recursive is easy. What about an iterative solution?

O(n) time
O(1) space
'''
def inorder_traversal(root):
  stack = []
  ans = []
  while stack or root:
    if root:
      stack.append(root)
      root = root.left
    else:
      last_node = stack.pop()
      ans.append(last_node.val)
      root = last_node.right
  return ans

        