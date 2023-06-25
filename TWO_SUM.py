class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums[i+1:]:
                result.append(i)
                result.append(nums.index(complement, i+1))
                break

        return result
s = Solution()
result = s.twoSum([2, 7, 11, 15], 9)
print(result)
