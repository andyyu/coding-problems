# Andy Yu
'''
You are playing the following Nim Game with your friend: 
There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. 
The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. 
Write a function to determine whether you can win the game given the number of stones in the heap.

Difficult: Easy

Solution Notes:
Not really a programming question per se, in that the optimum solution is simply math / logic based.
The immediately obvious "losing" position is if there are exactly 4 stones left, in which case no matter how many stones we take out, we lose.
We can then extrapolate from that position and realize that at 5, 6, or 7 stones are winning positions because we can simply take out the number of stones required to make the opponent play at 4 stones.
Therefore another losing position is at 8 - no matter how many stones we take out, the opponent is at a winning position (5, 6, 7).
Clearly, all multiples of 4 are losing positions.

O(1) time
O(1) space
'''
def can_win_nim(n):
  return n % 4 != 0