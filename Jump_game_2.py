class Solution:
    def jump(self, nums):
        n = len(nums)
        if n == 1:
            return 0
        
        jumps = 0
        curr_max_reach = 0
        next_max_reach = 0
        i = 0
        
        while i <= curr_max_reach:
            next_max_reach = max(next_max_reach, i + nums[i])
            
            if next_max_reach >= n - 1:
                return jumps + 1
            
            if i == curr_max_reach:
                curr_max_reach = next_max_reach
                jumps += 1
            
            i += 1
        
        return jumps
