class Solution:
    def spiralOrder(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        rowStart = 0
        rowEnd = m - 1
        colStart = 0
        colEnd = n - 1

        result = []

        while rowStart <= rowEnd and colStart <= colEnd:
            for i in range(colStart, colEnd + 1):
                result.append(matrix[rowStart][i])
            rowStart += 1

            for i in range(rowStart, rowEnd + 1):
                result.append(matrix[i][colEnd])
            colEnd -= 1

            if rowStart <= rowEnd:
                for i in range(colEnd, colStart - 1, -1):
                    result.append(matrix[rowEnd][i])
                rowEnd -= 1

            if colStart <= colEnd:
                for i in range(rowEnd, rowStart - 1, -1):
                    result.append(matrix[i][colStart])
                colStart += 1

        return result
