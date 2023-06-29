from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        
        for word in strs:
            # Sort the characters of the word
            sorted_word = ''.join(sorted(word))
            
            # Add the sorted word to the hashmap
            if sorted_word in anagram_map:
                anagram_map[sorted_word].append(word)
            else:
                anagram_map[sorted_word] = [word]
        
        # Return the values of the hashmap as the grouped anagrams
        return list(anagram_map.values())
