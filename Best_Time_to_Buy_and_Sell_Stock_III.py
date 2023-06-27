class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        
        # Initialize the buy and sell arrays
        buy1, buy2 = -prices[0], -prices[0]
        sell1, sell2 = 0, 0
        
        for i in range(1, n):
            # Update the first buy and sell values
            buy1 = max(buy1, -prices[i])
            sell1 = max(sell1, buy1 + prices[i])
            
            # Update the second buy and sell values
            buy2 = max(buy2, sell1 - prices[i])
            sell2 = max(sell2, buy2 + prices[i])
        
        return sell2
