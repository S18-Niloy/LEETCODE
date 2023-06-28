class Solution:
    def hIndex(self, citations):
        n = len(citations)
        counts = [0] * (n + 1)
        
        # Count the number of papers for each citation count
        for citation in citations:
            counts[min(citation, n)] += 1
        
        papers = 0
        
        # Traverse the counts from right to left to find the h-index
        for i in range(n, -1, -1):
            papers += counts[i]
            
            # Check if the researcher has published enough papers
            if papers >= i:
                return i
        
        return 0
