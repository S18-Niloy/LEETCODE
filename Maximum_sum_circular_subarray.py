class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadane(nums):
            max_sum = float('-inf')
            current_sum = 0

            for num in nums:
                current_sum = max(num, current_sum + num)
                max_sum = max(max_sum, current_sum)

            return max_sum

        total_sum = sum(nums)
        max_linear_sum = kadane(nums)
        max_circular_sum = total_sum + kadane([-num for num in nums])

        if max_circular_sum == 0:
            return max_linear_sum

        return max(max_linear_sum, max_circular_sum)
