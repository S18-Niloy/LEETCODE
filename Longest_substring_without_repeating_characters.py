class Solution:
    def lengthOfLongestSubstring(self, s):
        charSet = set()
        maxLen = 0
        left = 0
        
        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            
            charSet.add(s[right])
            maxLen = max(maxLen, right - left + 1)
        
        return maxLen
