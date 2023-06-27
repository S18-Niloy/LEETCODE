class Solution:
    def wordBreak(self, s, wordDict):
        # Create a set of words for efficient lookup
        wordSet = set(wordDict)

        # Create a list to track if a substring can be segmented
        dp = [False] * (len(s) + 1)
        dp[0] = True  # Empty string is always valid

        # Iterate through each substring of s
        for i in range(1, len(s) + 1):
            # Check if any prefix of the substring is valid
            for j in range(i):
                # If the prefix is valid and the remaining suffix is in the word set, mark dp[i] as True
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break

        # The last element of dp represents the validity of the entire string
        return dp[-1]
