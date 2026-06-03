"""
Reversing bits means that we reverse the position of each bit in the 32 space.

Example (n = 11):
Input:    00000000000000000000000000001011
Expected: 11010000000000000000000000000000
The solution needs to reverse 1011 to 1101 and then move that to the start of the 32 space.

Brute-force solution: At each position of a bit, just put it in the reverse index of the 32 bit space. We create
an array of 32 size and place each 1-bit to the reverse index.

Bit manipulation solution: Instead of using an array of 32 size, we can extract each bit and place it in the result
number at the reverse position without depending on an array.
"""
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            mask = 1 << i
            if mask & n:
                # place this 1-bit on reverse index
                reverse_i = 31 - i
                result |= 1 << reverse_i

        return result