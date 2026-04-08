class Solution:
    """
    Similar problem: Kth Largest Element in a Stream

    Solution 1: Min heap of size k, space is O(K)

    Solution 2: Quickselect
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums_s = sorted(nums)
        return nums_s[len(nums) - k]