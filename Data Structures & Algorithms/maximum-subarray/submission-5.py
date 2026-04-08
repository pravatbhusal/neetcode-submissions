class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kadane's algorithm O(N) time, O(1) space (greedy)
        # just ignore negative. if your sum is negative, then reset.
        # if your sum is still positive, then keep going.
        # very similar to sliding window since it's contigous array

        max = nums[0]
        cur = 0
        for num in nums:
            if cur < 0:
                # negative, so reset back
                cur = 0
            cur += num
            if cur > max:
                max = cur
        return max