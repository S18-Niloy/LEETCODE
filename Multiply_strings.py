class Solution:
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"

        n1, n2 = len(num1), len(num2)
        result = [0] * (n1 + n2)

        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')
                product = digit1 * digit2

                # Update the result array
                curr_sum = product + result[i + j + 1]
                result[i + j + 1] = curr_sum % 10
                result[i + j] += curr_sum // 10

        # Convert the result array to a string
        if result[0] == 0:
            result = result[1:]

        return ''.join(str(digit) for digit in result)
