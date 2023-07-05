class Solution:
    def reverseWords(self, s):
        words = s.split()  # Split string into words
        words.reverse()  # Reverse the order of words
        return ' '.join(words)  # Join the reversed words with a single space


s1 = "the sky is blue"
solution = Solution()
print(solution.reverseWords(s1))  # Output: "blue is sky the"

s2 = "  hello world  "
print(solution.reverseWords(s2))  # Output: "world hello"

s3 = "a good   example"
print(solution.reverseWords(s3))  # Output: "example good a"
