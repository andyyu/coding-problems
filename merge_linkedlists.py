# Andy Yu
'''
Merge two linked lists.
Difficulty: Easy

Solution notes:
O(n) time
O(1) space
using a temp node to solve. If no new nodes are allowed to be created, point to the smaller of the two linked list heads first.
'''

def merge_lists(head1, head2):
  if head1 is None:
        return head2
  if head2 is None:
        return head1
  ret = temp = node()
  while (head1 is not None) and (head2 is not None):
    if (head1 < head2):
      next_node = head1
      head1 = head1.next
    else:
      next_node = head2
      head2 = head2.next
    temp.next = next_node
    temp = temp.next
  temp.next = head2 if head1 is None else temp.next = head1
  return ret.next