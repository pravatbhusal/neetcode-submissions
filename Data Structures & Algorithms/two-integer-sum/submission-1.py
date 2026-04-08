class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for index, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                # found the matching pair
                start_index = seen[diff]
                return [start_index, index]
            else:
                # store this seen number
                seen[num] = index

        