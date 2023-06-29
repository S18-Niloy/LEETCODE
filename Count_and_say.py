class Solution:
    def countAndSay(self, n):
        if n == 1:
            return "1"

        prev = self.countAndSay(n - 1)
        count = 1
        result = ""
        
        for i in range(len(prev)):
            # Check if the current digit is the same as the next digit
            if i + 1 < len(prev) and prev[i] == prev[i + 1]:
                count += 1
            else:
                result += str(count) + prev[i]
                count = 1
        
        return result
