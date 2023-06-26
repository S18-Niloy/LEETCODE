from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        k = 1  # Number of unique elements
        count = 1  # Number of occurrences of the current element
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                count += 1
            else:
                count = 1
            
            if count <= 2:
                nums[k] = nums[i]
                k += 1
        
        return k

# Example usage
s = Solution()
nums = [1, 1, 1, 2, 2, 3]
k = s.removeDuplicates(nums)
print("Number of unique elements:", k)
print("Modified nums:", nums[:k])
