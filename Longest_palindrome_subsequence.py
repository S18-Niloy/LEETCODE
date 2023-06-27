class Solution:
    def longestPalindromeSubseq(self, s):
        n = len(s)

        # Create a 2D array to store the lengths of palindromic subsequences
        dp = [[0] * n for _ in range(n)]

        # Initialize the diagonal elements as 1 (single characters are palindromes)
        for i in range(n):
            dp[i][i] = 1

        # Iterate through the string in reverse order
        for i in range(n - 1, -1, -1):
            # Start from i + 1 since we only need to fill the upper triangle of the matrix
            for j in range(i + 1, n):
                # If the characters at positions i and j are the same
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        # The top-right element of the matrix contains the length of the longest palindromic subsequence
        return dp[0][n - 1]
