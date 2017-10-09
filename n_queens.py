# Andy Yu
'''
Given an n x n chessboard where n > 3, place n queens such that none of them are attacking each other.

--------------------------------------------------------------------------------

Difficulty: Medium

Solution notes:
backtracking / recursion

O(2^(n^2)) time (finding all solutions for n-queens is NP-Complete!)
O(n^2) space
'''
import copy

def is_safe(queen, n, board):
    row, col = queen[0], queen[1]
    if any([board[row][c] == 'Q' for c in xrange(n)]):
        return False
    if any([board[r][col] == 'Q' for r in xrange(n)]):
        return False
    while row >= 0 and col >= 0:
        if board[row][col] == 'Q':
            return False
        col -= 1
        row -= 1
    row, col = queen[0], queen[1]
    while row < n and col >= 0:
        if board[row][col] == 'Q':
            return False
        col -= 1
        row += 1
    return True

def place_queens(col, n, board, solutions):
    for row in xrange(n):
        if is_safe((row, col), n, board):
            board[row][col] = 'Q'
            if col+1 == n:
                solutions.append(copy.deepcopy(board))
            place_queens(col+1, n, board, solutions)
            board[row][col] = ' '
        else:
            continue

def get_solution(n):
    board = [[' ']*n for _ in xrange(n)]
    solutions = []
    place_queens(0, n, board, solutions)
    return solutions

def print_board(board):
    for row in board:
        print ''.join(['----' for _ in row]) + '-'
        print '| ' + ' | '.join([sq for sq in row]) + ' |'
    print ''.join(['----' for _ in row]) + '-'
    print '\n'

if __name__ == "__main__":
    result = get_solution(8)
    for board in result:
        print_board(board)
    print "Found {} solutions.".format(len(result))
