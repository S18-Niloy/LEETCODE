class Solution:
    def findLongestChain(self, pairs):
        # Sort the pairs based on the second element in ascending order
        pairs.sort(key=lambda x: x[1])
        
        count = 1
        current_end = pairs[0][1]
        
        # Iterate through the remaining pairs
        for i in range(1, len(pairs)):
            if pairs[i][0] > current_end:
                count += 1
                current_end = pairs[i][1]
        
        return count
