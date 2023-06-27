class Solution:
    def solveSudoku(self, board):
        """
        Solve the Sudoku puzzle by modifying the input board in-place.
        """
        if not board or len(board) != 9 or len(board[0]) != 9:
            return
        
        self.solve(board)
    
    def solve(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    for num in '123456789':
                        if self.isValid(board, row, col, num):
                            board[row][col] = num
                            
                            if self.solve(board):
                                return True
                            
                            board[row][col] = '.'  # Undo the choice if it leads to an invalid solution
                    return False  # No valid number found for this cell
        return True  # All cells are filled and the board is valid
    
    def isValid(self, board, row, col, num):
        # Check if the number already exists in the same row
        for i in range(9):
            if board[row][i] == num:
                return False
        
        # Check if the number already exists in the same column
        for j in range(9):
            if board[j][col] == num:
                return False
        
        # Check if the number already exists in the same 3x3 sub-grid
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == num:
                    return False
        
        return True
