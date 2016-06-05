# Andy Yu
'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: 
“The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Difficult: Easy

Solution Notes:

O(n) time
O(1) space
'''
def lowest_common_denominator(root, p, q)
  while root:
    if root.val > p.val and root.val > q.val:
      root = root.left
    elif root.val < p.val and root.val < q.val:
      root = root.right
    else:
      return root