class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kadane's algorithm O(N) time, O(1) space (greedy)
        # just ignore negative. if your sum is negative, then reset.
        # if your sum is still positive, then keep going.
        # very similar to sliding window since it's contigous array

        max_sum = nums[0]
        cur = 0
        for num in nums:
            if cur < 0:
                # negative, so reset back
                cur = 0
            cur += num
            max_sum = max(max_sum, cur)
        return max_sum