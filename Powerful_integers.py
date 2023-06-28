class Solution:
    def powerfulIntegers(self, x, y, bound):
        result = set()
        i = 0
        
        while x ** i <= bound:
            j = 0
            
            while x ** i + y ** j <= bound:
                result.add(x ** i + y ** j)
                j += 1
                
                if y == 1:
                    break
            
            i += 1
            
            if x == 1:
                break
        
        return list(result)
