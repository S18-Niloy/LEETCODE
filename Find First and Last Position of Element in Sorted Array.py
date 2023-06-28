class Solution:
    def searchRange(self, nums, target):
        # Initialize the starting and ending positions as -1
        start = -1
        end = -1

        # Find the starting position
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
            if nums[mid] == target:
                start = mid

        # Find the ending position
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
            if nums[mid] == target:
                end = mid

        # Return the starting and ending positions
        return [start, end]
