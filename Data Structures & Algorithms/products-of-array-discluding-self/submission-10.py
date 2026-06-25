"""
This is a classical "Prefix Sum" problem, but more specifically "Prefix Product".

We build a prefix[] array where prefix[i] is the running product excluding nums[i] from the left-side.
Meaning prefix[i] = product of nums from [0, ..., i - 1]

Prefix Product formula is: prefix[i] = prefix[i - 1] * nums[i - 1]

Example:
nums = [1, 2, 4, 6]
prefix[0] = 1 (base-case)
prefix[1] = prefix[0] * nums[0] = 1
prefix[2] = prefix[1] * nums[1] = 2
prefix[3] = prefix[2] * nums[2] = 8

Then we build a postfix[] array where postfix[i] is the running product excluding nums[i] from the right-side.
Meaning postfix[i] = product of nums from [i + 1, ..., n]

Postfix Product formula is: postfix[i] = postfix[i + 1] * nums[i + 1]

Example:
nums = [1, 2, 4, 6]
postfix[3] = 1 (base-case)
postfix[2] = postfix[3] * nums[3] = 1 * 6  = 6
postfix[1] = postfix[2] * nums[2] = 6 * 4  = 24
postfix[0] = postfix[1] * nums[1] = 24 * 2 = 48

The result is now: output[i] = prefix[i] * postfix[i]
In english, output[i] = (left running product where nums[i] is excluded) * (right running product where nums[i] is excluded)
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix product except self (left-side)
        prefix = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        # postfix product except self (right-side)
        postfix = [1] * len(nums)
        for i in range(len(nums) - 2, - 1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]

        # output
        output = []
        for i in range(len(nums)):
            output.append(prefix[i] * postfix[i])
        return output