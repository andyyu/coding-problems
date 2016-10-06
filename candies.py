# Andy Yu
'''
https://www.hackerrank.com/challenges/candies

Alice is a kindergarden teacher. 
She wants to give some candies to the children in her class.  
All the children sit in a line (their positions are fixed), and each  of them has a rating score according to his or her performance in the class.  
Alice wants to give at least 1 candy to each child. 
If two children sit next to each other, then the one with the higher rating must get more candies. 
Alice wants to save money, so she needs to minimize the total number of candies given to the children.

Input Format
The first line of the input is an integer N, the number of children in Alice's class. 
Each of the following N lines contains an integer that indicates the rating of each child.

Output Format
Output a single line containing the minimum number of candies Alice must buy.

Sample Input
3  
1  
2  
2

Sample Output
4

Explanation

Here 1, 2, 2 is the rating. Note that when two children have equal rating, they are allowed to have different number of candies. Hence optimal distribution will be 1, 2, 1.

Difficulty: Easy

Solution notes:
First though was to pass through, check if that child has a higher rating than the previous one.
If the new child has a higher rating, we give him 1 more candy than the previous child.
If the new child has a lower rating, we give him just 1 candy.

The only problem is in a sequence like [3, 2, 1], just one pass would leave all children with 1 candy.
So we have to "fix" all the other previous children whenever we hit a decreasing sequence.
The way I do it is to iterate through all the children again, from back to front - doing the same algorithm during this reverse pass.
The only difference for the reverse pass is we have to give a higher rated child max(original candies, prev child candy + 1) candies, since blindly giving him 1 more candy than the previous would undo the progress done by the first pass.

O(n) time
O(n) space
'''

import sys

input = sys.stdin.readlines()
input = input[1:]
candies = [1]*(len(input))
for i in xrange(1, len(input)):
    if input[i] > input[i-1]:
        candies[i] = candies[i-1] + 1
for i in xrange(len(input)-2, -1, -1):
    if input[i] > input[i+1]:
        candies[i] = max(candies[i], candies[i+1] + 1)
print sum(candies)
