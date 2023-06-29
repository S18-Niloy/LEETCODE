class Solution:
    def solveNQueens(self, n):
        results = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        cols = set()
        diagonals = set()
        anti_diagonals = set()
        self.backtrack(board, 0, cols, diagonals, anti_diagonals, results)
        return results

    def backtrack(self, board, row, cols, diagonals, anti_diagonals, results):
        if row == len(board):
            results.append(self.construct_solution(board))
            return

        for col in range(len(board)):
            if col in cols or (row + col) in diagonals or (row - col) in anti_diagonals:
                continue

            board[row][col] = 'Q'
            cols.add(col)
            diagonals.add(row + col)
            anti_diagonals.add(row - col)

            self.backtrack(board, row + 1, cols, diagonals, anti_diagonals, results)

            board[row][col] = '.'
            cols.remove(col)
            diagonals.remove(row + col)
            anti_diagonals.remove(row - col)

    def construct_solution(self, board):
        return [''.join(row) for row in board]
