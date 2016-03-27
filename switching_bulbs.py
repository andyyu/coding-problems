# Andy Yu
'''
There are n bulbs that are initially off. 
You first turn on all the bulbs. 
Then, you turn off every second bulb. 
On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). 
For the ith round, you toggle every i bulb. 
For the nth round, you only toggle the last bulb. 
Find how many bulbs are on after n rounds.

Naive solution: implement n rounds of bulb switching

With some thought, there is an O(1) solution.

Given this example where n = 4
[off, off, off, off]
[on, on, on, on]
[on, off, on, off]
[on, off, off, off]
[on, off, off, on]

We can see that each bulb is turned on / off during round k, if k is a factor of the bulb's number.
For example, bulb 3 is switched only on rounds 1 and 3, because 1 and 3 are the only factors of 3.
Likewise, bulb 4 is switched during rounds 1, 2, and 4 which are all factors of 4.
Additionally, since all bulbs are "off" from the start, we know a bulb will only be "on" at the end if it's switched an odd number of times.
When is a bulb switched an odd number of times? When it has an odd number of factors.
The only numbers that have an odd number of factors are perfect squares.
  (Proof) - All non-square numbers have factors 1 and itself, and all other factors are in pairs. Perfect squares k also have the factor sqrt(k) which gives them an odd number of factors.
  (Example) - 12 has factors (1, 12), and the pairs (2, 6), (3, 4)                                            : 6 total factors
              15 has factors (1, 15), and the pairs (3, 5)                                                    : 4 total factors
              16 (a perfect square) has factors (1, 16), and the pairs (2, 8), AND it's square root factor 4  : 5 total factors

Therefore, the number of bulbs "on" at the end are the number of bulbs in n bulbs that are perfect squares.
To count this, get the floor of the square root of n and that is the number of "square factors" of perfect squares.
For example: 17
floor of the square root of 17 is 4
4^2 = 16 (the largest perfect square in 17)
3^2 = 9
2^2 = 4
1^2 = 1

As we can see, all numbers from 1 to k (where k is the square root of the number of bulbs n), are the square factors of all perfect squares in n.
Any number bigger than k would represent a square factor that results in a perfect square not in n. (In our example, 5 would result in 5^2 = 25 > 17)
And every number from 1 to k (when squared) results in a perfect square from 1 to n.

'''
import math

def switch_bulbs(n):
  return int(math.sqrt(n))
