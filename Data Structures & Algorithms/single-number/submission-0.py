"""
XOR will flip the bits where 1 ^ 1 = 0, 0 ^ 1 = 1, 0 ^ 0 = 0.

We can run XOR on all nums and the remaining num would be the single number.
This is because if two same numbers exist, they would zero-out.

Ex: [3, 2, 3] = 3 ^ 2 ^ 3 = 2
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sum = 0
        for num in nums:
            sum ^= num
        return sum