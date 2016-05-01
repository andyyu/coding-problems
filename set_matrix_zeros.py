# Andy Yu
'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.


Solution notes:

My initial idea was to save the rows and columns that should be set to 0 in arrays, but that would take O(M+N) space, where
M and N are the numbers of rows and columns with 0 in it.

def set_zeros(matrix):
  rows = []
  columns = []
  for i in xrange(len(matrix)):
      for j in xrange(len(matrix[0])):
          if matrix[i][j] == 0:
              rows.append(i)
              columns.append(j)
  for i in xrange(len(matrix)):
      if i in rows:
          matrix[i] = [0]*len(matrix[i])
      else:
          for j in xrange(len(matrix[0])):
              if j in columns:
                  matrix[i][j] = 0

Instead, to do it with O(1) space complexity, I used the first row and first column as markers. 
I also need the first_row and first_col variables to record if the first row and first column must be set to 0 (because I'm using them as markers, I can't mark them).
'''

def set_zeros(matrix):
  first_row = False
  first_col = False
  for i in xrange(len(matrix)):
      for j in xrange(len(matrix[0])):
          if matrix[i][j] == 0:
              matrix[0][j] = 0
              matrix[i][0] = 0
              if i == 0:
                  first_row = True
              if j == 0:
                  first_col = True
  for i in xrange(1, len(matrix)):
      for j in xrange(1, len(matrix[0])):
          if matrix[0][j] == 0 or matrix[i][0] == 0:
              matrix[i][j] = 0
  if first_row:
      for j in xrange(len(matrix[0])):
          matrix[0][j] = 0
  if first_col:
      for i in xrange(len(matrix)):
          matrix[i][0] = 0
        