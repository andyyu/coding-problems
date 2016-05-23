# Andy Yu
'''
Given a set of candidate numbers (C) and a target number (T), 
find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7, 
A solution set is: 
[7] 
[2, 2, 3] 

Difficulty: Medium

Solution notes:
Use depth-first search. 
Code is fairly self explanatory, but gist of it is to recursively call dfs, adding 1 more number in candidate to the path, until we reach the target or over it.
If we reach the target, we add the path to the result, otherwise stop that path.
Some optimizations made: index was used because we should never add a smaller number than the latest in the path - both for speed and to avoid duplicate paths.
i.e. when making a path [2, 3] towards a target 7, we should never add another 2. 
This is why the loop that recursively calls dfs runs from (index, end).

https://leetcode.com/discuss/61491/asked-discuss-time-complexity-your-solution-what-would-say
'''
def combination_sum(candidates, target):
  res = []
  candidates.sort()
  dfs(candidates, target, 0, [], res)
  return res

def dfs(candidates, target, index, path, res):
  if target == 0:
    res.append(path)
    return
  for i in xrange(index, len(candidates)):
    if candidates[i] > target:
      break
    dfs(candidates, target-candidates[i], i, path + [candidates[i]], res)
