class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two sum (unsorted) was solved using dict O(N), check: i - seen = sum
        # this solution is O(1) space, hint: can only use pointers (two pointers)
        # left ptr is at 0, right ptr is at len - 1
        # move left when sum is less than target
        # move right when sum is greater than target

        left = 0
        right = len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]
            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                # return 1-indexed indices
                return [left + 1, right + 1]
