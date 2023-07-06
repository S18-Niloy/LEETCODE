class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        char_count = {}

        # Count the frequency of characters in s
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        # Decrement the count for characters in t
        for char in t:
            if char in char_count:
                char_count[char] -= 1
                if char_count[char] == 0:
                    del char_count[char]
            else:
                return False

        # If char_count is empty, all characters in s and t have matched
        return len(char_count) == 0
