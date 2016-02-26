# Andy Yu
'''
Check if two string inputs are anagrams of each other.
Difficulty: Easy

Solution: 
O(n) time
O(n) space
'''

def check_anagrams(word1, word2):
  letter_map = {}
  letter_map2 = {}
  for letter in word1:
    if letter in letter_map:
      letter_map[letter] += 1
    else:
      letter_map[letter] = 1
  for letter in word2:
    if letter in letter_map2:
      letter_map2[letter] += 1
    else:
      letter_map2[letter] = 1
  for letter in letter_map:
    if letter not in letter_map2:
      return False
    if not letter_map2[letter] == letter_map[letter]:
      return False
  return True
