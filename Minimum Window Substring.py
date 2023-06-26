from collections import Counter
class Solution:
    def minWindow(self,s, t):
        if len(s) < len(t):
            return ""

        target_count = Counter(t)
        window_count = Counter()
        formed = 0
        required = len(target_count)
        left = right = 0
        min_len = float('inf')
        min_window = ""

        while right < len(s):
            char = s[right]
            window_count[char] += 1

            if char in target_count and window_count[char] == target_count[char]:
                formed += 1

            while formed == required and left <= right:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_window = s[left:right+1]

                char = s[left]
                window_count[char] -= 1

                if char in target_count and window_count[char] < target_count[char]:
                    formed -= 1

                left += 1

            right += 1

        return min_window
