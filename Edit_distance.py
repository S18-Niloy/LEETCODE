class Solution:
    def minDistance(self, word1, word2):
        m = len(word1)
        n = len(word2)

        # Create a 2D array to store the minimum number of operations
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Initialize the first row and column with incremental values
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        # Compute the minimum number of operations for each substring
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # If the characters at positions i and j are the same, no operation is needed
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # Find the minimum of insert, delete, and replace operations
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

        # The last element of the matrix contains the minimum number of operations
        return dp[m][n]
