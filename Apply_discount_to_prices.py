class Solution:
    def discountprices(self, sentence: str, discount: int) -> str:
        words = sentence.split()
        result = []

        for word in words:
            if word.startswith('$') and word[1:].isdigit():
                price = float(word[1:])
                discount_price = price * (1 - discount / 100)
                updated_word = f"${discount_price:.2f}"
                result.append(updated_word)
            else:
                result.append(word)

        return ' '.join(result)
