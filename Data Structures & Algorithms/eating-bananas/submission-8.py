"""
The solution must return the fastest rate of k.
k ranges from [1, max(piles)] where 1 = fastest rate and max(piles) = slowest rate

We must search for the smallest k in that range that satifisfies eating within h hours.
The range [1, max(piles)] is sorted, so we can perform a binary search.

When do we move left ptr? When k is too slow we can't eat in h hours.
When do we move right ptr? When k is too fast we had extra time in h hours.
Answer is k == min time to eat in h hours, which is the left ptr of binary search.
"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left <= right:
            k = (left + right) // 2

            # time to eat bananas at this k rate
            time = 0
            for p in piles:
                time += math.ceil(float(p) / k)
            if time > h:
                # eating too slow, go faster
                left = k + 1
            else:
                # eating too fast, slow down
                right = k - 1

        return left