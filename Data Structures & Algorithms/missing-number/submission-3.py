"""
Math solution:
Get the sum of the list from [0, len(nums)] assuming there is no duplicate number. Then get the actual sum of the nums list.
Subtract the sum minus the actual sum to get the missing number.

However, in a real interview, this would fail because the interviewer is looking for a bit-wise solution!

XOR solution:
Similar Problem: "Single Number"
In that solution, we use an XOR operator to find the only number that isn't duplicated in the list.
Now, in this solution we negate each number i at nums[i]. The remainder would be that missing number.
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        
        remainder = n
        for i in range(n):
            # use XOR to negate each number i at nums[i]
            remainder ^= i ^ nums[i]

        # remainder after negation is the missing number
        return remainder