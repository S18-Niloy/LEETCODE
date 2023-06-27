class Solution:
    def longestPalindrome(self, s):
        """
        Find the longest palindromic substring in the given string s.
        """
        if not s:
            return ""
        
        n = len(s)
        start = 0
        max_length = 1
        
        # Initialize a 2D table to store the results of subproblems
        dp = [[False] * n for _ in range(n)]
        
        # All substrings of length 1 are palindromes
        for i in range(n):
            dp[i][i] = True
        
        # Check substrings of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_length = 2
        
        # Check substrings of length greater than 2
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    start = i
                    max_length = length
        
        return s[start:start + max_length]
