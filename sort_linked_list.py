# Andy Yu
'''
Sort a linked list in O(n log n) time using constant space complexity.

--------------------------------------------------------------------------------

Difficulty: Medium

Solution notes:

Use merge sort (in place - merging linked lists).
Use walker and runner pointers to find the midpoint of the linked list.
(If runner moves two nodes for every one node walker moves,
then the walker will be at the middle node when the runner reaches the end.)
Split the linked list at the midpoint and recursively call merge() on both
linked lists. Merge using a basic merge() function on the two linked lists.

O(n log n) time
O(1) space
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def sort_list(head):
    if head is None or head.next is None:
        return head
    walker = head
    runner = head.next.next
    while runner is not None and runner.next is not None:
        runner = runner.next.next
        walker = walker.next
    halfway_node = walker.next
    walker.next = None
    return merge(sort_list(head), sort_list(halfway_node))

def merge(list1, list2):
    head = tail = ListNode(0)
    while list1 or list2:
        if list1 is not None:
            if (list2 and list1.val <= list2.val) or list2 is None:
                tail.next = list1
                list1 = list1.next
                tail = tail.next
        if list2 is not None:
            if (list1 and list2.val <= list1.val) or list1 is None:
                tail.next = list2
                list2 = list2.next
                tail = tail.next
    return head.next
