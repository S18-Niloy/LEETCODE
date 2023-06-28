class Solution:
    def longestSubsequence(self, arr, difference):
        dp = {}
        
        for num in arr:
            prev_num = num - difference
            if prev_num in dp:
                dp[num] = dp[prev_num] + 1
            else:
                dp[num] = 1
        
        return max(dp.values())
