class Solution:
    def generateParenthesis(self, n):
        result = []
        self.backtrack(n, n, "", result)
        return result
    
    def backtrack(self, left_count, right_count, current, result):
        # Base case: If both left and right counts are zero, we have formed a valid combination
        if left_count == 0 and right_count == 0:
            result.append(current)
            return
        
        # We can add a left parenthesis if there are remaining left parentheses
        if left_count > 0:
            self.backtrack(left_count - 1, right_count, current + "(", result)
        
        # We can add a right parenthesis if there are remaining right parentheses
        if right_count > left_count:
            self.backtrack(left_count, right_count - 1, current + ")", result)
