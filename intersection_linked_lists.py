# Andy Yu
'''
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.

Difficult: Easy

Solution Notes:
We just need to "sync" the pointers and negate the offset created by the difference between the lengths of the linked lists.
We do this by switching the paths of our two pointers from one linked list to the other, so after 1 pass they should be primed to encounter the collision.

O(2max(m, n)) time
O(1) space

'''
def get_intersection_node(headA, headB):
  pointA = headA
  pointB = headB
  while pointA != pointB:
    pointA = pointA.next if pointA else headB
    pointB = pointB.next if pointB else headA
  return pointA
