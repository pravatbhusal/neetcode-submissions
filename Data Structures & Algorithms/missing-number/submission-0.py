"""
Get the sum of the list from [0, len(nums)] assuming there is no duplicate number. Then get the actual sum of the nums list.
Subtract the sum minus the actual sum to get the missing number.
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected = n * (n + 1) // 2 # Math formula: n × (n + 1) / 2 = 0 + 1 + 2 + ... + n
        return expected - sum(nums)