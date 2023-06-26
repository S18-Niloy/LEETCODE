class Solution:
    def candy(self, ratings):
        n = len(ratings)
        candies = [1] * n

        # Traverse from left to right, ensuring higher rated children have more candies than their left neighbors
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Traverse from right to left, ensuring higher rated children have more candies than their right neighbors
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        # Calculate the total number of candies needed
        total_candies = sum(candies)

        return total_candies
