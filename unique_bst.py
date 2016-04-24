# Andy Yu
'''
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

Difficulty: Medium

Solution notes:

Dynamic programming! I first started by thinking of the way to create unique binary search trees.
For example, trying to find all unique BSTs for n=3, you'd want to choose 1 number to act as the root and then build the numbers from there.
You'd have a minimum of 3 different BSTs with roots 1, 2, 3. 
Then, to build the rest of the BST, it's basically the same strategy (picking the next "root") out of the remaining numbers.
This way, we can calculate the total # of unique BSTs of a given n by iterating over n chosen "roots" 1-n and then for each 
chosen root, add the # of possible left subtree BSTs times the # of right subtree BSTs.

n = 0;     null   
count[0] = 1

n = 1;      1       
count[1] = 1 

n = 2;    1__                    __2     
              \                 /                 
             count[1]       count[1]    

count[2] = 1 + 1 = 2


n = 3;    1__                     __2__                    __3
              \                 /       \                 /     
          count[2]        count[1]    count[1]      count[2]

count[3] = 2 + 1 + 2  = 5


n = 4;    1__                   __2__                      ___3___                  
              \              /        \                   /       \         
          count[3]       count[1]    count[2]         count[2]   count[1]

             __4                
           /
       count[3]   

count[4] = 5 + 2 + 2 + 5 = 14 

O(n^2) time
O(n) space
'''

def numTrees(self, n):
  if n == 0 or n == 1:
      return 1
  res = [0]*(n+1)
  res[0] = 1
  res[1] = 1
  for num in xrange(2, n+1):
      for i in xrange(1, num+1):
          res[num] += res[i-1]*res[num-i]
  return res[n]