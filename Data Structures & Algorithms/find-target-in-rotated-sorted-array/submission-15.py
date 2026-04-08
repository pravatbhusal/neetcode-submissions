class Solution:
    # similar problem: Find Minimum in Rotated Sorted Array
    # find the point where the array was rotated. this would be the value where n - 1 is greater than n.
    # example: [5, 6, 7, 1, 2] <- point is at 1
    # at point, there are two sorted lists: [5, 6, 7] and [1, 2]
    # if target is greater than point, then binary search the right list else search left list.
    # solution has two separate binary searches: one search to find the point and second to find the target

    def search(self, nums: List[int], target: int) -> int:
        point_i = self.find_pivot(nums)

        # edge case if pivot point is the target itself
        if target == nums[point_i]:
            return point_i

        # which of the two split lists has target?
        if nums[0] <= nums[len(nums) - 1]:
            # edge case where the nums is already sorted (no pivot point)
            left = 0
            right = len(nums) - 1
        elif target > nums[point_i] and target < nums[0]:
            # target is small, search from right split list
            left = point_i
            right = len(nums) - 1
        else:
            # target is large, search from left split list
            right = point_i - 1
            left = 0

        # binary search the split list
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                # too small, move right
                left = mid + 1
            else:
                # too large, move left
                right = mid -1
        
        return -1

    # how can we binary search the point where point - 1 is greater than point? 
    # ex: list is [3, 4, 5, 6, 1, 2]. if i'm at 5, how do i know i need to move to the right?
    # well the beginning of the list is 3 which is less than 5, so we know that the split is on the right side.
    # then we move to 2, and we see that the beginning of the list 3 is less than 2. so we know split is on left side.
    # then we move to 1 and we are done.
    def find_pivot(self, nums):
        # edge case where the nums is already sorted (no pivot point)
        if nums[0] <= nums[len(nums) - 1]:
            return 0

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if mid > 0 and nums[mid - 1] > nums[mid]:
                # found the point
                return mid
            if nums[0] <= nums[mid]:
                # move right
                left = mid + 1
            else:
                # move left
                right = mid - 1
        return 0
        

