# Andy Yu
'''
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

Difficulty: Medium

Solution notes: *WARNING - VERY WORDY EXPLANATION AHEAD. SKIP TO BOTTOM TO SEE SOLUTION*

We can very easily do this linearly, but that wouldn't be very fun, would it?
To solve this in logarithmic time we can approach this like binary search. 
"But the numbers aren't sorted!", you might say -- but the only necessity for a binary-like search is that we can "choose" which half of the set to look at next. 
In binary search we "choose" based on the value of the number we're looking for compared to the middle value we're currently looking at 
(if search_value < middle, search again in the subset left of the middle point, else search in the right).

In this case, we must establish how we can decide whether to look in the left or right half next to search for our peak.
On a side note, the base case is that the middle point we have found is a peak. In which case, we just return the middle index.
Otherwise, we must choose to search either left half or right half of the middle point.
We can abuse the idea that num[i] != num[i+1], and that num[-1] = num[n] = -∞. 
Let's imagine the cases where either the left or right half do NOT contain a peak. How can this happen?
For the left subset, it can only not contain a peak if it's in perfect ascending order.
For example, if we're looking at this set:
[1, 2, 4, 5, 8, 9, 10, 13, 14]
and we choose "8" to be the middle value, then the left subset does not contain a peak since it's in ascending order.
If it wasn't ascending, there would either a) have to be a "typical" peak, or b) the first number would be a peak since num[-1] = -∞ (try it out!)
For the right subset, it can only NOT contain a peak if it's in perfect DESCENDING order.
If it wasn't descending, there would either a) have to be a peak, or b) the last number would be a peak (again, try finding a counter-example!)
Therefore, we can conclude that the right subset must have a peak if the number right of the middle point is greater (then it wouldn't be descending).
If the number right of the middle point isn't greater (then the right subset could potentially not have a peak), then the number left of the middle point must be less -
because if they were both greater than our middle point would be a peak. Then, the left subset must not be perfectly ascending and therefore has a peak.

Using this knowledge, we can break our algorithm down like this.

1) pick a middle point
2) check if it's a peak. If so, return.
3) if the number right of the middle is greater, then look in the right half, else look in the left half
4) pick a new middle and repeat 3-4
5) we should have either found the peak, or we are left with 2 numbers left in our search subset - in which case, return the greater of the two.

O(logn) time
O(n) space
'''

def find_peak_element(nums):
  start = 0
  end = len(nums)-1
  while start < end-1:
    middle = end+start/2
    if nums[middle] > nums[middle-1] and nums[middle] < nums[middle+1]: # "base" case, middle is a peak
        return middle
    if nums[middle+1] > nums[middle]:
        start = middle+1
    else:
        end = middle-1
  return start if nums[start] >= nums[end] else end
