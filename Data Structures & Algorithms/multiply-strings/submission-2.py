"""
My solution (not possible due to int size limit):
Convert num1 into a number by % 10 each digit and dividing by 10.
Convert num2 into a number by % 10 each digit and dividing by 10.
Multiply the two numbers to get the result. Convert result to string and return.

WRONG: Multiplying two big ints is a problem because the whole point is that the product can
be too large to fit in standard integer size 2^31.
"""
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str((int(num1) * int(num2)))