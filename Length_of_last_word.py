class Solution:
    def lengthOfLastWord(self, s):
        s = s.strip()  # Remove leading and trailing spaces
        last_word = s.split(" ")[-1]  # Split string by spaces and get the last word
        return len(last_word)
