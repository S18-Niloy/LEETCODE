class Solution:
    def generate(self, numRows):
        triangle = []

        for row in range(numRows):
            # Initialize a new row with 1's at the beginning and end
            current_row = [1] * (row + 1)

            # Calculate the values for the middle of the row
            for i in range(1, row):
                current_row[i] = triangle[row - 1][i - 1] + triangle[row - 1][i]

            triangle.append(current_row)

        return triangle
