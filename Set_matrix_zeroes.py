class Solution:
    def setZeroes(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        # Create two sets to store the row and column indices
        # where we need to set zeroes
        zero_rows = set()
        zero_cols = set()

        # Iterate over the matrix and mark the row and column indices
        # where we encounter zeroes
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        # Iterate over the matrix again and set the entire row and column
        # to zeroes if their indices are present in the zero_rows and zero_cols sets
        for i in range(rows):
            for j in range(cols):
                if i in zero_rows or j in zero_cols:
                    matrix[i][j] = 0

        return matrix
