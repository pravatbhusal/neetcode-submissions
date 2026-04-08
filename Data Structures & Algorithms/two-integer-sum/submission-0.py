class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_map = dict()
        for i in range(len(nums)):
            num = nums[i]
            diff = target - num
            if diff in diff_map:
                # found a diff that sums to the target
                return [diff_map[diff], i]
            else:
                # cannot find a diff, store i for next iteration
                diff_map[num] = i
        