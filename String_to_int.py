class Solution:
    def myAtoi(self, s):
        """
        Convert the string s to a 32-bit signed integer.
        """
        s = s.strip()  # Remove leading and trailing whitespace
        
        if not s:
            return 0
        
        sign = 1
        result = 0
        i = 0
        
        if s[i] == '-' or s[i] == '+':
            if s[i] == '-':
                sign = -1
            i += 1
        
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            result = result * 10 + digit
            
            # Clamp the result if it goes beyond the 32-bit signed integer range
            if sign == 1 and result >= 2**31:
                return 2**31 - 1
            elif sign == -1 and result >= 2**31:
                return -2**31
            
            i += 1
        
        return sign * result
