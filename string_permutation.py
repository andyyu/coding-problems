# Andy Yu
'''
Print all permutations of a string.
Difficulty: Easy

Solution notes:
O(n*n!) time
O(1) space
'''

def permutate(string, prefix = ''):
  if (len(string) == 0):
    print prefix
  else:
    for char in string:
      permutate(string[:string.index(char)] + string[string.index(char)+1:], prefix + char)

