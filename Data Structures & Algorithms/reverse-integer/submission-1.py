"""
Extract each bit from the end of the number x using % 10 and dividing by / 10.
"""
class Solution:

    def reverse(self, x: int) -> int:
        original = x
        MIN_INT = -2 ** 31
        MAX_INT = (2 ** 31) - 1
        
        result = 0
        while x:
            # extract last digit
            digit = abs(x) % 10
            x = int(x / 10)

            # add digit to result
            result = (result * 10) + digit

            # handle overflow
            if result > MAX_INT or result < MIN_INT:
                return 0
        
        return result if original > 0 else -result