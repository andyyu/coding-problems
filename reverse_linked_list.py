# Andy Yu
'''
Reverse a linked list.
Difficulty: Easy

Solution notes:
Recursion! 
'''

def reverse(head, last=None):
  if head is None
    return last
  next = head.next
  head.next = last
  return reverse(next, head)