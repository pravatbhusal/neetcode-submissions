class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
 
        # solution: use a dict. check if nums[i] + 1 in dict.
        # store the smallest start of a sequence as the dict value
        # if encounter new smallest start, then recheck sequence.
        nums_d = dict()
        for num in nums:
            nums_d[num] = sys.maxsize

        largest = 1
        for num in nums:
            next = num + 1
            if next in nums_d and num < nums_d[next]:
                # found new smallest start of a sequence
                cur = 1
                while next in nums_d:
                    nums_d[next] = num
                    next += 1
                    cur += 1
                largest = max(cur, largest)
        return largest

