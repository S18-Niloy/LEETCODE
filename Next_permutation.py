class Solution:
    def nextPermutation(self, nums):
        n = len(nums)

        # Find the first decreasing element from right to left
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # If no decreasing element found, the array is in descending order,
        # so we reverse it to get the lowest possible order
        if i == -1:
            nums.reverse()
            return

        # Find the smallest element larger than nums[i] to its right
        j = n - 1
        while j > i and nums[j] <= nums[i]:
            j -= 1

        # Swap nums[i] and nums[j]
        nums[i], nums[j] = nums[j], nums[i]

        # Reverse the elements from i+1 to the end
        left = i + 1
        right = n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
