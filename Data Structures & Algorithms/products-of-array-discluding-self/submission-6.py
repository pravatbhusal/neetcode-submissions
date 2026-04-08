class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not len(nums):
            return []
        # get total product of all items in one iteration
        # then in another iteration divide by nums[i]

        # count number of zeroes for edge case
        zeroes = 0
        for num in nums:
            if num == 0:
                zeroes += 1
        if zeroes > 1:
            # edge case - all will be zero
            return [0] * len(nums)

        # get total product - O(N) time
        total_product = nums[0]
        total_product_no_zero = nums[0] if nums[0] != 0 else 1
        for i in range(1, len(nums)):
            total_product *= nums[i]
            total_product_no_zero *= nums[i] if nums[i] != 0 else 1

        # create except_self array dividing by nums[i] - O(N) time & space
        except_self = list()
        for num in nums:
            if num != 0:
                except_self.append(int(total_product / num))
            else:
                # edge case - there's only 1 zero number
                except_self.append(total_product_no_zero)
        return except_self