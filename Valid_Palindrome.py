class Solution:
    def isPalindrome(self, s: str) -> bool:
        import string
        y = s.translate(str.maketrans('', '', string.punctuation))

        y= y.lower()
        y="".join(y.split())
        a = len(y)
        z = len(y)//2
        result = None
        if a%2==1:
            if y[:z]==y[z+1:][::-1]:
                result = True
            else:
                result = False
        else:
            if y[:z]==y[z:][::-1]:
                result = True
            else:
                result = False
        return result

s = Solution()
result = s.isPalindrome("A man, a plan, a canal: Panama")
print(result)
