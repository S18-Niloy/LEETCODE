class Solution:
    def reverse(self, x: int) -> int:
        if x>0:
            reversed_num = int(str(x)[::-1])
        elif x < 0:
            reversed_num = -1 * int(str(-1*x)[::-1])
        else:
            reversed_num = int(str(x)[::-1])
        
        if reversed_num>2**31 or reversed_num<-2**31:
            reversed_num=0
        return reversed_num

s = Solution()
print(s.reverse(123))
