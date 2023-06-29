from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start):
            if start == len(nums):
                # Add the current permutation to the result
                result.append(nums[:])
            else:
                used = set()
                for i in range(start, len(nums)):
                    # Check if the current number has been used in this position
                    if nums[i] in used:
                        continue
                    # Mark the current number as used
                    used.add(nums[i])
                    # Swap the current element with the element at index 'start'
                    nums[start], nums[i] = nums[i], nums[start]
                    # Recursively generate permutations for the remaining elements
                    backtrack(start + 1)
                    # Restore the original order by swapping back
                    nums[start], nums[i] = nums[i], nums[start]
        
        result = []
        backtrack(0)
        return result
