# Andy Yu
'''
From: Cracking the Coding Interview 6th ed. #1.6

Implement a method to perform basic string compression using the counts of repeated characters.
For example, the string aabcccccaaa would become a2b1c5a3.
If the "compressed" string would not become smaller than the original string, your method should return the original string.
You can assume the string has only uppercase and lowercase letters (a-z).

Difficulty: Easy

Solution notes:


O(n) time
O(n) space
'''

def string_compression(input):
  count = 0
  letter = input[0]
  result = []
  for i in input:
    if i == letter:
        count += 1
    else:
        result.append(letter+str(count))
        count = 1
        letter = i
  result.append(letter+str(count))
  return ''.join(result)

if __name__ == '__main__':
  print string_compression("aabcccccaaa")