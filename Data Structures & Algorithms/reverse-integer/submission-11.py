"""
Extract each bit from the end of the number x using % 10 and dividing by / 10.
Before updating the result, we must check for int overflow.

The input x is a 32-bit signed integer, so x = (-2^31, 2^31 - 1)
If handle the reverse with abs(x), we need to handle edge-case of
-2^31 because we cannot abs that value as a positive integer.
"""
class Solution:

    def reverse(self, x: int) -> int:
        MAX_INT = (2 ** 31) - 1
        MIN_INT = -2 ** 31

        # edge-case before abs(x)
        if x == MIN_INT:
            return 0
        
        original = x
        x = abs(x)
        result = 0
        while x:
            # extract last digit
            digit = x % 10
            x = int(x / 10)

            # check int overflow before updating result
            if result > MAX_INT // 10 or (result == MAX_INT // 10 and digit > MAX_INT % 10):
                return 0

            # add digit to result
            result = (result * 10) + digit
        
        return result if original > 0 else -result