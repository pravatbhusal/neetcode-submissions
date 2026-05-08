"""
Maximum Subarray tells me Kadane's algorithm. But unlike the Maximum Sum Subarray problem, multiplying two negatives
can lead to a positive number. This makes it trickier to know when to reset the greedy algorithm.

Kadane's algorithm for max sum subarray was solved using the recurrence function: dp[i] = max(nums[i], dp[i-1] + nums[i])
We only need to store 1 variable for dp[i - 1] so it was O(1) space, but underlying it's a DP problem.

Can we make a similar recurrence function for this max product subarray problem?
Let's break this down into a subproblems.
Example: nums = [1, 2, -3, 4]
[1] -> max = 1
[1, 2] -> max = 2
[1, 2, -3] -> max = 2
[1, 2, -3, 4] -> max = 4

Example: nums = [4, -1, 2, -2]
[4] -> max = 4
[4, -1] -> max = 4
[4, -1, 2] -> max = 4
[4, -1, 2, -2] -> max = 16

At the last element -2, how did you "know" to multiply it with 4 * -1 * 2 = -8? What were you implicitly tracking?
This tells me we need to track both the positive and negative cases.

The positive case becomes the largest number (the maximum).
The negative case becomes the smallest number (the minimum).

Recurrence function (max case): max_product = max(max_product * nums[i], min_product * nums[i])
Recurrence function (min case): min_product = min(max_product * nums[i], min_product * nums[i])
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        min_product = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            temp_max_product = max_product
            max_product = max(max_product * nums[i], min_product * nums[i], nums[i])
            min_product = min(temp_max_product * nums[i], min_product * nums[i], nums[i])
            result = max(max_product, result)

        return result