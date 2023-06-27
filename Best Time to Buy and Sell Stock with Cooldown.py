class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0

        n = len(prices)

        # Create two arrays to store the maximum profits for each day with or without stock in hand
        dp_hold = [0] * n
        dp_not_hold = [0] * n

        dp_hold[0] = -prices[0]

        for i in range(1, n):
            if i == 1:
                dp_hold[i] = max(dp_hold[i - 1], -prices[i])
            else:
                dp_hold[i] = max(dp_hold[i - 1], dp_not_hold[i - 2] - prices[i])
            dp_not_hold[i] = max(dp_not_hold[i - 1], dp_hold[i - 1] + prices[i])

        # The maximum profit will be obtained when not holding any stock
        return dp_not_hold[n - 1]
