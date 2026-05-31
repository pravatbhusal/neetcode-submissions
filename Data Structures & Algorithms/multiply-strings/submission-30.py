"""
My solution (not possible due to int size limit):
Convert num1 into a number by % 10 each digit and dividing by 10.
Convert num2 into a number by % 10 each digit and dividing by 10.
Multiply the two numbers to get the result. Convert result to string and return.

WRONG: Multiplying two big ints is a problem because the whole point is that the product can
be too large to fit in standard integer size of 32 bytes. num2.length == 200, which is 84 bytes!

Long multiplication solution (from 3rd grade math class):
In math class, when we multiply two large numbers we multiply digit-by-digit in reverse and store a carry-over digit.
If we use that same process, we only need to append the product of two digits to the result and store a carry-over digit.

Ex: 123 * 456
      1 2 3
    * 4 5 6
    -------
      7 3 8   ← 123 * 6
    6 1 5 0   ← 123 * 5, shifted left 1
  4 9 2 0 0   ← 123 * 4, shifted left 2
  ---------
  5 6 0 8 8

The max possible result size is len(num1) + len(num2).
"""
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = [0] * (len(num1) + len(num2))
        
        # long multiplication algorithm
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, - 1):
                # add the product
                product = int(num1[i]) * int(num2[j])
                res[i + j + 1] += product
                # add the carry to left
                res[i + j] += res[i + j + 1] // 10
                # keep only the ones digit
                res[i + j + 1] %= 10

        # remove trailing 0s, convert to str, and return
        return "".join(map(str, res)).lstrip("0") or "0"