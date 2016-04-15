# Andy Yu
'''
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:
For the return value, each inner list's elements must follow the lexicographic order.
All inputs will be in lower-case.

Difficulty: Medium

Solution notes:

Clever fast and short solution using Python tricks
d = collections.defaultdict(list)
for s in strs:
   d[tuple(sorted(s))].append(s)  
return [a for agram_group in d.values() if len(agram_group)>1 for a in agram_group]

O(n) time
O(n) space
'''
def group_anagrams(strs):
  d = {}
  for s in sorted(strs): # first sort to ensure inner list lexicographic order
      key = "".join(sorted(s))  # this is the un-anagrammed key for each word, 'bac' gives key 'abc'
      d[key] = d.get(key, []) + [s]   # map -> key: 'abc', value: ['bac', 'cab', 'acb', etc.]
  return [wl for wl in d.values()]
