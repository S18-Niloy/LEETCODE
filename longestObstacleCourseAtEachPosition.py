class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles):
        n = len(obstacles)

        # Create a list to store the lengths of the longest obstacle course at each position
        dp = []
        ans = []

        for height in obstacles:
            # Find the index where the current obstacle can be inserted in the sorted dp list
            index = self.binarySearch(dp, height)

            # Update the dp list and ans list
            if index == len(dp):
                dp.append(height)
                ans.append(index + 1)
            else:
                dp[index] = height
                ans.append(index + 1)

        return ans

    def binarySearch(self, dp, target):
        left, right = 0, len(dp) - 1
        while left <= right:
            mid = (left + right) // 2
            if dp[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return left
