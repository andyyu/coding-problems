# Andy Yu
'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3

But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.


--------------------------------------------------------------------------------

Difficulty: Easy

Solution notes:
Just track through examples manually (how do you know if a tree is symmetric by looking at it?), then convert to code.

O(n) time
O(1) space
'''

def isSymmetric(root):
        if root is None:
            return True
        else:
            return isMirror(root.left, root.right)

def isMirror(left, right):
    if left is None or right is None:
        return left is None and right is None
    if left.val == right.val:
        return isMirror(left.left, right.right) and isMirror(left.right, right.left)
    else:
        return False

def isSymmetricIterative(self, root):
    if root is None:
        return True
    else:
        stack = [(root.left, root.right)]
        while len(stack) > 0:
            pair = stack.pop()
            left = pair[0]
            right = pair[1]
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val == right.val:
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
            else:
                return False
        return True
