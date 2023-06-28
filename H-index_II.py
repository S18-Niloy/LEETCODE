class Solution:
    def hIndex(self, citations):
        n = len(citations)
        left, right = 0, n - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            h = n - mid
            
            if citations[mid] == h:
                return h
            elif citations[mid] < h:
                left = mid + 1
            else:
                right = mid - 1
        
        return n - left
