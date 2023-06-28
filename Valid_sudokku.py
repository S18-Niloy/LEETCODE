class Solution:
    def isValidSudoku(self, board):
        # Initialize sets to keep track of seen digits in rows, columns, and sub-boxes
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        # Traverse the Sudoku board
        for i in range(9):
            for j in range(9):
                # Get the current digit
                digit = board[i][j]
                # Skip if the cell is empty
                if digit == ".":
                    continue
                
                # Check if the digit already exists in the current row
                if digit in rows[i]:
                    return False
                rows[i].add(digit)
                
                # Check if the digit already exists in the current column
                if digit in columns[j]:
                    return False
                columns[j].add(digit)
                
                # Check if the digit already exists in the current sub-box
                box_index = (i // 3) * 3 + j // 3
                if digit in boxes[box_index]:
                    return False
                boxes[box_index].add(digit)
        
        # The Sudoku board is valid
        return True
