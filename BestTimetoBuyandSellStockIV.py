class Solution:
    def maxProfit(self, k, prices):
        if k == 0 or not prices:
            return 0

        n = len(prices)

        # If k is larger than the number of available transactions, we can treat it as an unlimited number of transactions
        if k >= n // 2:
            return self.maxProfitUnlimited(prices)

        # Create two 2D arrays to store the maximum profits for each day and transaction
        dp_buy = [[0] * (k + 1) for _ in range(n)]
        dp_sell = [[0] * (k + 1) for _ in range(n)]

        for i in range(k + 1):
            dp_buy[0][i] = -prices[0]

        for i in range(1, n):
            for j in range(1, k + 1):
                dp_buy[i][j] = max(dp_buy[i - 1][j], dp_sell[i - 1][j - 1] - prices[i])
                dp_sell[i][j] = max(dp_sell[i - 1][j], dp_buy[i - 1][j] + prices[i])

        # The maximum profit will be obtained from the last sell operation
        return dp_sell[n - 1][k]

    def maxProfitUnlimited(self, prices):
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit
