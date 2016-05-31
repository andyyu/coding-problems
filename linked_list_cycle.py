# Andy Yu
'''
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?

Solution Notes:
Floyd's cycle finding algorithm.

My first solution looked something like this:
  def has_cycle(head):
    if head == None or head.next == None:
      return False
    walker = head
    runner = head.next
    while walker.next and runner.next and runner.next.next:
      if walker.val == runner.val:
        return True
      walker = walker.next
      runner = runner.next.next
    return False
But upon further inspection, there are some clear inefficiencies.
For one, our while loop invariant is very ugly. (We need to check runner.next before runner.next.next because trying to access 'next' if runner.next is None will throw an error)
With some thought, I realized we don't actually have to check if walker.next, because it will always "follow" the runner.
By simply changing the order when we change / check runner and walker, we can really cut down the code.

O(n) time
O(1) space
'''
def has_cycle(head):
  walker = runner = head
  while runner and runner.next:
    runner = runner.next.next
    walker = walker.next
    if walker == runner:
      return True
  return False

