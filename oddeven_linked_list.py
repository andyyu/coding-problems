# Andy Yu
'''
Given a singly linked list, group all odd nodes together followed by the even nodes. 
Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input. 
The first node is considered odd, the second node even and so on ...

Difficult: Medium

Solution Notes:
Use two running linked lists (odd / even) and combine at end

O(n) time
O(1) space
'''
def odd_even_list(head):
  if not head:
    return None
  if not head.next:
    return head
  ret1 = odd = head
  ret2 = even = head.next
  head = head.next.next
  while head:
    odd.next = head
    even.next = head.next
    odd = odd.next
    even = even.next
    head = head.next.next if even else None
  odd.next = ret2
  return ret1

