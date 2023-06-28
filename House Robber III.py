class Solution:
    def rob(self, root):
        def helper(node):
            if not node:
                return (0, 0)
            
            left = helper(node.left)
            right = helper(node.right)
            
            rob_curr = node.val + left[1] + right[1]
            not_rob_curr = max(left) + max(right)
            
            return (rob_curr, not_rob_curr)
        
        result = helper(root)
        return max(result)
