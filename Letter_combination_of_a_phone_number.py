class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        combinations = []
        self.generateCombinations(digits, digit_to_letters, '', combinations)
        return combinations
    
    def generateCombinations(self, digits, digit_to_letters, current, combinations):
        if not digits:
            combinations.append(current)
            return
        
        for letter in digit_to_letters[digits[0]]:
            self.generateCombinations(digits[1:], digit_to_letters, current + letter, combinations)
