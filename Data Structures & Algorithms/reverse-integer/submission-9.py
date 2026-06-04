"""
Extract each bit from the end of the number x using % 10 and dividing by / 10.
"""
class Solution:

    def reverse(self, x: int) -> int:
        original = x
        MAX_INT = (2 ** 31) - 1
        
        result = 0
        while x:
            # extract last digit
            digit = abs(x) % 10
            x = int(x / 10)

            # check int overflow before updating result
            if result > MAX_INT // 10 or (result == MAX_INT // 10 and digit > MAX_INT % 10):
                return 0

            # add digit to result
            result = (result * 10) + digit
        
        return result if original > 0 else -result