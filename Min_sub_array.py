class Solution:
    def minSubArrayLen(self, target, nums):
        n = len(nums)
        left = 0
        min_len = float('inf')
        current_sum = 0

        for right in range(n):
            current_sum += nums[right]

            while current_sum >= target:
                min_len = min(min_len, right - left + 1)
                current_sum -= nums[left]
                left += 1

        if min_len == float('inf'):
            return 0
        else:
            return min_len
Console
