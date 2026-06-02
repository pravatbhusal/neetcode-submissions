"""
Use a bit mask on each bit position from i = 0 to i = 32.
The mask is (1 << i), which results in:
i = 0 -> (1 << 0) = 1
i = 1 -> (1 << 1) = 10
i = 2 -> (1 << 2) = 100
i = 3 -> (1 << 3) = 1000
etc.

This mask would test the single 1-bit on each position of n.

Ex: 0001 & 1011 = 0001 (has 1)
Ex: 0010 & 1011 = 0010 (has 1)
Ex: 0100 & 1011 = 0000 (has 0)
Ex: 1000 & 1011 = 1000 (has 1)
The answer is 3.
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for i in range(32):
            mask = 1 << i
            if mask & n:
                # 1-bit exists on i
                res += 1
        return res