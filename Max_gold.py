class Solution:
    def getMaximumGold(self, grid):
        max_gold = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(row, col, curr_gold):
            nonlocal max_gold  # Specify that max_gold is a non-local variable

            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
                return

            gold = grid[row][col]
            curr_gold += gold
            max_gold = max(max_gold, curr_gold)

            # Mark the current cell as visited
            grid[row][col] = 0

            # Explore the neighboring cells
            dfs(row - 1, col, curr_gold)  # Up
            dfs(row + 1, col, curr_gold)  # Down
            dfs(row, col - 1, curr_gold)  # Left
            dfs(row, col + 1, curr_gold)  # Right

            # Restore the value of the current cell
            grid[row][col] = gold

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != 0:
                    dfs(row, col, 0)

        return max_gold
