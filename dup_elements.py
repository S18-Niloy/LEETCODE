from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        k = 1  # Number of unique elements
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        
        return k

# Example usage
s = Solution()
nums = [1, 1, 2, 2, 2, 3, 4, 4, 5]
k = s.removeDuplicates(nums)
print("Number of unique elements:", k)
print("Modified nums:", nums[:k])
