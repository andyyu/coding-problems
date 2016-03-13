# Andy Yu
'''
In Jim's Burger, n hungry burger fans are ordering burgers. 
The ith order is placed by the ith fan at t time and it takes d time to process. 
What is the order in which the fans will get their burgers? 
(read from std: write to stdout)

Sample input:
8 1
4 2
5 6
3 1
4 3

Output:
4 2 5 1 3

Difficulty: Easy

Solution notes:
O(n) time
O(n) space
'''

import sys

orders = {}
input = sys.stdin.readlines()
for i in xrange(0, len(input)):
    orders[i] = sum(int(x) for x in input[i].split())    # map order i to its finished time
print ' '.join(str(x) for x in sorted(orders, key=orders.get))    # sort by finished time

