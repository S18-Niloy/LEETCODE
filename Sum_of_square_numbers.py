class Solution:
    def judgeSquareSum(self, c):
        left, right = 0, int(c ** 0.5)
        
        while left <= right:
            sum_of_squares = left * left + right * right
            
            if sum_of_squares == c:
                return True
            elif sum_of_squares < c:
                left += 1
            else:
                right -= 1
        
        return False
