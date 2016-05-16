# Andy Yu
'''
You are given two linked lists representing two non-negative numbers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

Difficulty: Easy

Solution notes:
O(n) time
O(1) space
'''

def add_two_numbers(l1, l2):
  output = pointer = ListNode(0)
  carry = 0
  while l1 or l2:
    val = carry
    if l1:
      val += l1.val
      l1 = l1.next
    if l2:
      val += l2.val
      l2 = l2.next
    carry = (val - (val%10))/10
    val = val % 10
    pointer.next = ListNode(val)
    pointer = pointer.next
  if carry != 0:
    pointer.next = ListNode(carry)
  return output.next

