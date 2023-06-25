class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        z = len(y)//2
        result = None
        if y[:z]==y[z+1:]:
            result = True
        else:
            result = False

        return result

s = Solution()
result = s.isPalindrome(121)
print(result)
            
