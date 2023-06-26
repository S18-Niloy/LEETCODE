from collections import Counter
class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_len = len(words[0])
        window_len = len(words) * word_len
        words_count = Counter(words)
        result = []

        for i in range(len(s) - window_len + 1):
            window = s[i:i+window_len]
            window_count = Counter([window[j:j+word_len] for j in range(0, window_len, word_len)])

            if window_count == words_count:
                result.append(i)

        return result
