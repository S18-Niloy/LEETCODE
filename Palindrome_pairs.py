class Solution:
    def palindromePairs(self, words):
        def is_palindrome(word):
            return word == word[::-1]

        word_to_index = {word: i for i, word in enumerate(words)}
        palindrome_pairs = []

        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                prefix = word[:j]
                suffix = word[j:]

                if is_palindrome(prefix):
                    reversed_suffix = suffix[::-1]
                    if reversed_suffix in word_to_index and word_to_index[reversed_suffix] != i:
                        palindrome_pairs.append([word_to_index[reversed_suffix], i])

                if j != len(word) and is_palindrome(suffix):
                    reversed_prefix = prefix[::-1]
                    if reversed_prefix in word_to_index and word_to_index[reversed_prefix] != i:
                        palindrome_pairs.append([i, word_to_index[reversed_prefix]])

        return palindrome_pairs
