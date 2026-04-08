class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search for the rotated point where the list is split
        # point = point's left element is greater than point element
        # to find min, check first element of both lists

        if len(nums) <= 1:
            return nums[0]

        low = 0
        high = len(nums) - 1

        if nums[low] <= nums[high]:
            # array is already sorted
            return nums[low]

        while low <= high:
            mid = int((low + high) / 2)
            if nums[mid - 1] > nums[mid]:
                # this is the point
                if nums[mid] < nums[0]:
                    return nums[mid]
                else:
                    nums[0]
            if nums[0] <= nums[mid]:
                # move to right if 0th element is less than mid
                low = mid + 1
            else:
                # move to left if 0th element is greater than mid
                high = mid - 1
