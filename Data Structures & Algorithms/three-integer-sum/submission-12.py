class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # two sum was solved using a dict and storing seen values
        # then subtracting seen values from current i check if = to sum

        # three sum might work using 2 pointers
        # store each i in the sublist, then find 2 pointers till sum = 0
        # total time = O(N^2), space = O(N)

        # another solution is sort the list (two sum II)
        # then use 2 left & right pointers that shift till sum = 0
        # total time = O(N^2), space = O(N)

        s_nums = sorted(nums)
        result = []
        for i, num in enumerate(s_nums):
            # to prevent dups, the prev i cannot be the same as i
            # otherwise the same list will be re-created
            if i != 0 and s_nums[i] == s_nums[i - 1]:
                continue

            left = i + 1
            right = len(s_nums) - 1
            while left < right:
                total = s_nums[left] + s_nums[right] + num
                if total == 0:
                    result.append([s_nums[left], s_nums[right], num])
                    left += 1

                    # to prevent dups, skip left until finding distinct number
                    while s_nums[left] == s_nums[left - 1] and left < right:
                        left += 1
                elif total > 0:
                    # too large
                    right -= 1
                else:
                    # too small
                    left += 1
        return result
        