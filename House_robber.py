class Solution:
    def rob(self, nums: List[int]) -> int:
        # Handle base cases
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # Create a DP table to store the maximum amount of money robbed at each house
        dp = [0] * len(nums)
        
        # Base cases: the maximum amount of money robbed at the first and second houses
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        # Fill the DP table iteratively
        for i in range(2, len(nums)):
            # The maximum amount of money robbed at the current house is the maximum
            # of robbing the current house plus the maximum amount robbed at two houses ago,
            # or skipping the current house and taking the maximum amount robbed at the previous house
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        
        return dp[-1]
