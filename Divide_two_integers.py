class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle division by zero
        if divisor == 0:
            return 2**31 - 1

        # Handle overflow cases
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        # Convert dividend and divisor to positive
        is_negative = (dividend < 0) != (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0
        while dividend >= divisor:
            temp = divisor
            multiple = 1

            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            dividend -= temp
            quotient += multiple

        if is_negative:
            quotient = -quotient

        return quotient
