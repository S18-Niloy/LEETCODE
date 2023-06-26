class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorial = [1]
        for i in range(1, n):
            factorial.append(factorial[-1] * i)
        
        nums = [str(i) for i in range(1, n + 1)]
        k -= 1  # Adjust k to 0-based index
        
        result = []
        for i in range(n - 1, -1, -1):
            idx = k // factorial[i]
            result.append(nums[idx])
            nums.pop(idx)
            k %= factorial[i]
        
        return ''.join(result)
