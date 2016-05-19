# Andy Yu
'''
Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.

Inputs are l1 and l2, both ListNodes (or None)
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


Difficulty: Easy

Iterative method is listed below. You can also do this recursively:
def merge_lists(l1, l2):
  if not l1 or not l2:
    return l1 or l2
  if l1.val > l2.val:
    l2.next = merge_lists(l1, l2.next)
    return l2 
  else:
    l1.next = merge_lists(l1.next, l2)
    return l1

Solution notes:
O(n) time
O(1) space
'''

def merge_lists(l1, l2):
  ret = []
  while l1 or l2:
    if l1 and (not l2 or l1.val < l2.val):
      ret.append(l1.val)
      l1 = l1.next
    else:
      ret.append(l2.val)
      l2 = l2.next
  return ret

