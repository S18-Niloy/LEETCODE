class Solution:
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                return [left + 1, right + 1]  # Adjust indices by one since they are 1-indexed
            
            if current_sum < target:
                left += 1
            else:
                right -= 1
        
        return []  # No solution found
