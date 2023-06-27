from collections import Counter

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # Create a frequency counter for the numbers in the array
        freq = Counter(nums)
        
        # Determine the maximum number in the array
        max_num = max(nums)
        
        # Create a DP table to store the maximum points earned up to each number
        dp = [0] * (max_num + 1)
        
        # Base case: the maximum points earned for the first number
        dp[1] = freq[1]
        
        # Iterate over the numbers, calculating the maximum points earned
        for i in range(2, max_num + 1):
            # Two options: either delete the current number and add its points,
            # or skip the current number and take the maximum points from the previous number
            dp[i] = max(dp[i - 1], dp[i - 2] + i * freq[i])
        
        return dp[max_num]
