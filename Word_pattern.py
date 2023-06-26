class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        pattern_to_word = {}
        word_to_pattern = {}

        for char, word in zip(pattern, words):
            if char not in pattern_to_word and word not in word_to_pattern:
                pattern_to_word[char] = word
                word_to_pattern[word] = char
            elif char in pattern_to_word and pattern_to_word[char] != word:
                return False
            elif word in word_to_pattern and word_to_pattern[word] != char:
                return False

        return True
