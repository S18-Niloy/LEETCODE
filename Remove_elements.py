from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] == val:
                nums[left] = nums[right]
                right -= 1
            else:
                left += 1
        return left

s = Solution()
nums = [3, 2, 2, 3]
val = 3
new_length = s.removeElement(nums, val)
print("New Length:", new_length)
print("Modified nums:", nums[:new_length])
