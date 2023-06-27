class Solution:
    def minimumDeleteSum(self, s1, s2):
        m = len(s1)
        n = len(s2)

        # Create a 2D array to store the lowest ASCII sum of deleted characters
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Compute the lowest ASCII sum of deleted characters for each substring
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # If the characters at positions i and j are the same, no characters need to be deleted
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # Find the minimum of deleting from s1 or s2
                    dp[i][j] = min(dp[i - 1][j] + ord(s1[i - 1]), dp[i][j - 1] + ord(s2[j - 1]))

        # The last element of the matrix contains the lowest ASCII sum of deleted characters
        return dp[m][n]
