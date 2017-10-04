# Andy Yu
'''
Determine if a Sudoku is valid, according to: http://sudoku.com.au/TheRules.aspx

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

Difficulty: Medium

Problem solutions:
Split the problem into subproblems - checkLine() and checkSquare()

O(n^2) time
O(n) space
'''

class Solution(object):
    def checkSquare(self, square):
        print(square)
        nums = [1]*10
        for row in square:
            for num in row:
                if num == '.':
                    continue
                if nums[int(num)] == 0:
                    return False
                nums[int(num)] = 0
        return True

    def checkLine(self, row):
        nums = [1]*10
        for num in row:
            if num == '.':
                continue
            if nums[int(num)] == 0:
                return False
            nums[int(num)] = 0
        return True

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in board:
            if not self.checkLine(row):
                return False
        for col_num in xrange(len(board[0])):
            column = [row[col_num] for row in board]
            if not self.checkLine(column):
                return False
        x = 0
        y = 0
        while x < len(board[0]):
            while y < len(board):
                square = [board[row][x:x+3] for row in xrange(y, y+3)]
                if not self.checkSquare(square):
                    return False
                y += 3
            x += 3
            y = 0
        return True


# Short solution

def isValidSudoku(board):
  seen = []
  for i, row in enumerate(board):
      for j, c in enumerate(row):
          if c != '.':
              seen += [(c,j),(i,c),(i/3,j/3,c)]
  return len(seen) == len(set(seen))
