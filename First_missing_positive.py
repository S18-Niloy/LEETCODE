class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Perform cyclic sort
        i = 0
        while i < len(nums):
            # Check if the current number can be placed in its correct position
            if 1 <= nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]:
                # Swap the current number with the number at its correct position
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            else:
                i += 1

        # Find the first missing positive integer
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1

        # If all positive integers are present, return the next positive integer
        return len(nums) + 1
