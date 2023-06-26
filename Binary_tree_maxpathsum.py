class Solution:
    def maxPathSum(self, root):
        self.max_sum = float('-inf')  # Initialize max_sum as negative infinity

        # Recursive helper function to calculate the maximum path sum
        def maxPathSumHelper(node):
            if not node:
                return 0

            left_sum = max(maxPathSumHelper(node.left), 0)  # Calculate maximum sum in the left subtree
            right_sum = max(maxPathSumHelper(node.right), 0)  # Calculate maximum sum in the right subtree

            # Calculate the maximum path sum passing through the current node
            current_sum = node.val + left_sum + right_sum

            # Update max_sum if the current path sum is greater
            self.max_sum = max(self.max_sum, current_sum)

            # Return the maximum sum from the current node to its parent
            return node.val + max(left_sum, right_sum)

        maxPathSumHelper(root)  # Start the recursive function from the root
        return self.max_sum
