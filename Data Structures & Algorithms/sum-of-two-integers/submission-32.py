"""
Cannot use arithmetic operators, so we'll use bitwise operators.

Example: a = 4, b = 7, result = 11
a =      00100
b =      00111
result = 01011

Example: a = 1, b = 1, result = 2
a =      01
b =      01
result = 10

I'm thinking we need to XOR each bit and use a carry bit to the left.
The hard part is moving that carry on each i and double-count the carry
from prev i and current i.
"""
class Solution:
    def getSum(self, a: int, b: int) -> int:
        result = 0
        carry = 0
        for i in range(32):
            mask = 1 << i
            bit_a = 1 if a & mask else 0
            bit_b = 1 if b & mask else 0
            # put xor bit on position i with the carry from prev i
            xor_mask = (bit_a ^ bit_b ^ carry) << i
            result |= xor_mask
            # set carry for the next i
            carry = 1 if (bit_a and bit_b) or (bit_a and carry) or (bit_b and carry) else 0
        
        max_pos_int = 0x7FFFFFFF # 01111111... = 2^31 - 1
        mask = 0xFFFFFFFF
        if result > max_pos_int:
            # result is negative, convert unsigned result into twos complement
            return ~(result ^ mask)
        return result