# Andy Yu
'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.

Difficult: Easy

Solution Notes:

Originally used a 'feeler' pointer to find the next non-duplicate node (like below), but quickly realized that it was not necessary.
def delete_duplicates(head):
  ptr = head
  while ptr:
    feeler = ptr
    while feeler.next and feeler.next.val == feeler.val:
      feeler = feeler.next
    ptr.next = feeler.next
    ptr = ptr.next
  return head

O(n) time
O(1) space
'''
def delete_duplicates(head):
  ptr = head
  while ptr:
    while ptr.next and ptr.next.val == ptr.val:
      ptr.next = ptr.next.next
    ptr = ptr.next
  return head

