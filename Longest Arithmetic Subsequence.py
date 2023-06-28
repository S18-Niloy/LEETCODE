class Solution:
    def longestArithSeqLength(self, nums):
        n = len(nums)
        dp = [{} for _ in range(n)]
        result = 2
        
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                if diff in dp[j]:
                    dp[i][diff] = dp[j][diff] + 1
                else:
                    dp[i][diff] = 2
                result = max(result, dp[i][diff])
        
        return result
