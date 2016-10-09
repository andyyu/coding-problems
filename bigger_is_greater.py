# Andy Yu
'''
Given a word w, rearrange the letters of w to construct another word s in such a way that s is lexicographically greater than w. 
In case of multiple possible answers, find the lexicographically smallest one among them.

Input Format

The first line of input contains t, the number of test cases. Each of the next t lines contains w.

Constraints

1 <= t <= 10^5
1 <= |w| <= 100
w will contain only lower-case English letters and its length will not exceed .

Output Format

For each testcase, output a string lexicographically bigger than w in a separate line. 
In case of multiple possible answers, print the lexicographically smallest one, and if no answer exists, print no answer.

== Sample Input ==
5
ab
bb
hefg
dhck
dkhc

== Sample Output ==
ba
no answer
hegf
dhkc
hcdk

== Explanation == 
Test case 1: 
There exists only one string greater than ab which can be built by rearranging ab. That is ba.
Test case 2: 
Not possible to rearrange bb and get a lexicographically greater string.
Test case 3: 
hegf is the next string lexicographically greater than hefg.
Test case 4: 
dhkc is the next string lexicographically greater than dhck.
Test case 5: 
hcdk is the next string lexicographically greater than dkhc.

Difficulty: Medium

Solution notes:
Initial thought, we want to iterate over all the letters from the end to the front. 
We should be looking for the first letter that we can swap with one behind it to make the string lexicographically bigger.
In: D K H C A
We would look at A first. No swap.
Look at C. Can't swap with A because its bigger than A.
Look at H. Can't swap with C or A because its bigger.
Look at K. Can't swap.
Look at D. First to be able to swap (we can swap with either K or H behind it). We should then swap with the smallest one larger than D (H).
Checking all of these letters to see if it's swappable would take n^2 time, but we can just use the idea that as long as the letters continue increasing, they are not swappable.
As soon as we hit a letter that is smaller than the one before it (D is smaller than K, in this case), we know that there must be a letter behind it that is lexicographically smaller.
New step: once we find the "swapping" letter, sort the end sequence of letters past it. 
Swapping D and H would produce: H K D C A. However, this is not the correct answer yet. We must sort the end sequence past the original swapped letter's index (0).
This means we have to sort H [KDCA] <- this part, to become H A C D K, which is the correct answer.
Normally sorting would take n log n time, but luckily we have the convenient property in that we iterated from back to front waiting for a non-lexicographically increasing number / letter - meaning that it's already sorted (in descending order).
All we have to do is reverse it.

O(n) time
O(n) space
'''

import sys

  # this function swaps two characters in indices (from, to) in the string
def swap(string, frm, to):
    char_list = list(string)
    char_list[frm], char_list[to] = char_list[to], char_list[frm]
    return ''.join(char_list)

def order_lex(word):
    prev = 0
    i = len(word)-1
    while len(word) > 1 and i>0 and word[i] >= prev:  # iterate from end to front, stop when we either reach the front or hit a decreasing letter
        prev = word[i]
        i -= 1
    if word[i] >= prev: # check if we reached the front of the string without finding a swapable letter
        return "no answer"
    swap_index = i
    while i < len(word) and word[swap_index] <= word[i]:  # iterate back towards the end to find the smallest lexicographically-larger letter to swap with
        i += 1
    swap2_index = i-1
    word = swap(word, swap_index, swap2_index)  # swap
    return word[:swap_index+1] + word[swap_index+1:][::-1]  # reverse the last section past the swap index

input_lines = sys.stdin.readlines()
for i in xrange(1, len(input_lines)):
   print order_lex(input_lines[i].strip('\n')) 

