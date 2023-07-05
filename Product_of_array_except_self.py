class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        left_products = [1] * n
        right_products = [1] * n
        answer = [1] * n

        # Calculate the product of all elements to the left of each element
        for i in range(1, n):
            left_products[i] = left_products[i - 1] * nums[i - 1]

        # Calculate the product of all elements to the right of each element
        for i in range(n - 2, -1, -1):
            right_products[i] = right_products[i + 1] * nums[i + 1]

        # Multiply the left and right products to get the final answer
        for i in range(n):
            answer[i] = left_products[i] * right_products[i]

        return answer
