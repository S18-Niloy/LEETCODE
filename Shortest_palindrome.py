class Solution:
    def shortestPalindrome(self, s):
        if not s:
            return ""

        reversed_s = s[::-1]
        n = len(s)

        for i in range(n):
            if s[:n - i] == reversed_s[i:]:
                return reversed_s[:i] + s

        return ""
