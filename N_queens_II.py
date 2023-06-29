class Solution:
    def totalNQueens(self, n):
        self.count = 0
        board = [['.' for _ in range(n)] for _ in range(n)]
        self.backtrack(board, 0)
        return self.count

    def backtrack(self, board, row):
        if row == len(board):
            self.count += 1
            return

        for col in range(len(board)):
            if self.is_valid(board, row, col):
                board[row][col] = 'Q'
                self.backtrack(board, row + 1)
                board[row][col] = '.'

    def is_valid(self, board, row, col):
        # Check if the current position is under attack

        # Check the same column
        for i in range(row):
            if board[i][col] == 'Q':
                return False

        # Check the diagonal from top-left to bottom-right
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        # Check the diagonal from top-right to bottom-left
        i, j = row - 1, col + 1
        while i >= 0 and j < len(board):
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        return True
