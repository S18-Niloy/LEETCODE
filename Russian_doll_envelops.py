class Solution:
    def maxEnvelopes(self, envelopes):
        # Sort the envelopes based on width in ascending order.
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        # Create a list to store the heights of the envelopes.
        heights = [envelope[1] for envelope in envelopes]

        # Apply binary search with dynamic programming.
        dp = []
        for height in heights:
            left, right = 0, len(dp)
            while left < right:
                mid = (left + right) // 2
                if dp[mid] < height:
                    left = mid + 1
                else:
                    right = mid
            if right == len(dp):
                dp.append(height)
            else:
                dp[right] = height

        # The length of dp represents the maximum number of nested envelopes.
        return len(dp)
