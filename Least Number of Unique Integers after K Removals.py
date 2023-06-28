class Solution:
    def findLeastNumOfUniqueInts(self, arr, k):
        freq_map = {}
        for num in arr:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        freq_counts = sorted(freq_map.values())
        unique_count = 0
        for count in freq_counts:
            if k >= count:
                k -= count
            else:
                return len(freq_counts) - unique_count
            
            unique_count += 1
        
        return 0
