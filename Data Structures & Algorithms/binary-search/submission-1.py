class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # two pointers - low and high
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = int((high + low) / 2)
            if target > nums[mid]:
                # target is larger, move to right-side
                low = mid + 1
            elif target < nums[mid]:
                # target is lower, move to left-side
                high = mid -1
            else:
                return mid
        return -1

