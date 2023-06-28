class Solution:
    def findNumberOfLIS(self, nums):
        n = len(nums)
        lengths = [1] * n  # Initialize lengths array with all 1's
        counts = [1] * n   # Initialize counts array with all 1's
        
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if lengths[j] + 1 > lengths[i]:
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
                    elif lengths[j] + 1 == lengths[i]:
                        counts[i] += counts[j]
        
        max_length = max(lengths)
        result = 0
        
        for i in range(n):
            if lengths[i] == max_length:
                result += counts[i]
        
        return result
