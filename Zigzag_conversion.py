class Solution:
    def convert(self, s, numRows):
        """
        Convert the string s into a zigzag pattern with numRows rows.
        """
        if numRows == 1 or numRows >= len(s):
            return s
        
        result = [''] * numRows
        index, step = 0, 1
        
        for char in s:
            result[index] += char
            
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            
            index += step
        
        return ''.join(result)
