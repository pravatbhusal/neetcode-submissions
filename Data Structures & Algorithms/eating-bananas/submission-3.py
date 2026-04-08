class Solution:
    # piles[0] = 5, so there are 5 of bananas in 1st pile
    
    # we need to decide a value k where we eat k bananas per 1 hour.
    # example: k = 5, so i eat 5 bananas per hour. this means piles[0] will be completely eaten after 1 hour.
    # i cannot eat from another pile in that same hour.

    # we need to find the smallest rate per hour (k) where we can eat all bananas in h hours
    # ex: k = 1, h = 5. it will take 5 hours to eat all bananas.

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # ex: [3, 6, 7, 11] and h = 8, the answer is k = 4
        # hint #1 mentioned to find upper bound of k. that would be the largest value in the list.
        # keep decreasing from the largest value till we find the min possible value for k
        # if we sort the array, then we can binary search until the above condition is met

        # find largest value
        max_pile = max(piles)

        # now search for the min possible k
        left = 1
        right = max_pile
        while left <= right:
            k = (left + right) // 2

            # count number of hours it would take to eat at rate k
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)

            # is this the min possible value of k?
            if hours <= h:
                # koko ate too fast, eat slower next time (decrease k)
                right = k - 1
            else:
                # koko ate too slow, eat faster next time (increase k)
                left = k + 1


        return left
