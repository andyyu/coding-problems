# Andy Yu
'''
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. 

(https://leetcode.com/problems/letter-combinations-of-a-phone-number/#_=_)

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Difficulty: Medium
'''

def letterCombinations(self, digits):
    if not digits:
        return []
    mapping = {"1":[""], "2":['a', 'b', 'c'], "3":['d', 'e', 'f'], "4":['g', 'h', 'i'], "5":['j', 'k', 'l'], "6":['m', 'n', 'o'], "7":['p', 'q', 'r', 's'], "8":['t', 'u', 'v'], "9":['w', 'x', 'y', 'z']}
    solutions = [[] for _ in xrange(len(digits)+1)]
    solutions[0].append("")
    for i, n in enumerate(digits):
        for prefix in solutions[i]:
            for letter in mapping[n]:
                solutions[i+1].append(prefix+letter)
    return solutions[-1]
        

