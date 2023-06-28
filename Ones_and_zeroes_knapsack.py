class Solution:
    def findMaxForm(self, strs, m, n):
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for s in strs:
            count_zero = s.count('0')
            count_one = len(s) - count_zero
            
            for i in range(m, count_zero - 1, -1):
                for j in range(n, count_one - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - count_zero][j - count_one] + 1)
        
        return dp[m][n]
