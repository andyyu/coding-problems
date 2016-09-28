# Andy Yu
'''
A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative. 
The first difference (if one exists) may be either positive or negative. 
A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive and negative. 
In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.

Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. 
A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.

Examples:
Input: [1,7,4,9,2,5]
Output: 6
The entire sequence is a wiggle sequence.

Input: [1,17,5,10,13,15,10,5,16,8]
Output: 7
There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].

Input: [1,2,3,4,5,6,7,8,9]
Output: 2

Difficult: Easy - Medium

Solution Notes:
We can do this in one pass with this simple algorithm in mind.
Iterate over the numbers in the input, keeping track of the wiggle direction (positive or negative).
If the numbers follow the wiggle pattern, simply append to the solution list, switch the wiggle direction and continue.
Otherwise, if a number breaks the wiggle pattern, we can simply remove the last number we added.
The logic behind this is that if it breaks the wiggle pattern, that number must be more extreme in sequence than the previous number.
Example:
2, 4, 9 <- The positive case: 9 breaks the wiggle so it must be larger (more extreme in the positive wiggle) than 4
8, 5, 1 <- The negative case: 1 breaks the wiggle so it must be smaller (more extreme in the negative wiggle) than 5
Since we must clearly either remove the current number or the one before (since they contradict each other in the wiggle sequence), we should just choose the one before because it does not offer as extreme as a wiggle by nature.
For example, given [2, 4, 9] we must remove either 4 or 9. What if the input continued [2, 4, 9, 6]?
If we removed 9, then [2, 4, 6] would hit another contradiction whereas removing 4 produces [2, 9, 6], which successfully extends the wiggle sequence.

O(n) time
O(n) space

'''
def max_wiggle_length(nums):
  if not nums:  # if nums is length 0, return 0
    return 0
  diff_pos = None   # use diff_pos to keep track of the wiggle direction
  solution = [nums[0]]    # initialize solution list with first number in the input
  for num in nums[1:]:    # iterate over the rest of the numbers in the input
    if num == solution[-1]:   # if the number is equal to the one before it, ignore it
      continue
    elif diff_pos is None:    # if the wiggle direction hasn't been initialized yet, calculate it
      diff_pos = (num > solution[-1])
      solution.append(num)
    else:
      if ((num > solution[-1]) != diff_pos):   # if successful wiggle
        diff_pos = not diff_pos
        solution.append(num)
      else:   # breaks wiggle sequence, remove previous number
        solution.pop()
        solution.append(num)
  return len(solution)
