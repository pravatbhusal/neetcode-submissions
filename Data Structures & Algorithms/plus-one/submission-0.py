"""
The problem asks us to convert the digits list into the number,
then add 1 and return the result.

In reverse, multiply each digit by a factor of 10 and as we iterate to the
next index increase the multiplication factor by another 10.
i = 0, factor = 1; i = 1, factor = 10; i = 2, factor = 100; etc.
Ex [1, 2, 3, 4]: (4 * 1) + (3 * 10) + (2 * 100) + (1 * 1000) = 1234
"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        factor = 1
        sum = 0

        # multiply in reverse by an increasing factor of 10
        for i in range(len(digits) - 1, -1, -1):
            sum += digits[i] * factor
            factor *= 10
        
        # plus one
        sum += 1

        # re-convert back into list
        result = []
        while sum >= 1:
            result.append(sum % 10)
            sum //= 10
        result.reverse()
        return result