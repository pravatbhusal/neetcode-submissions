"""
This is a subarray DP problem. Bursting a balloon at nums[i] shrinks the
array and changes its neighbors, making it very hard to track what the
neighbors of future bursts will be.

Instead of thinking about which balloon to burst first, we think about
which balloon to burst last in a given window [l, r]. If balloon i is the
last to burst in [l, r], then at the moment it pops, everything else
inside the window is already gone — so its only neighbors are the stable
window boundaries nums[l-1] and nums[r+1].

Ex: nums = [4,2,3,7] --> [4,3,7] --> [4,7] --> [7] --> []
In reverse: [] --> [7] --> [4,7] --> [4,3,7] --> [4,2,3,7]

We pad nums with 1s on each side to handle out-of-bounds neighbors.

Recursive algorithm (top-down divide and conquer with memoization):
1. For window [l, r], try every index i as the last balloon to burst
2. Divide into two independent subproblems:
    a. helper(l, i-1): burst everything to the left of i first
    b. helper(i+1, r): burst everything to the right of i first
3. Then pop i last: coins = nums[l-1] * nums[i] * nums[r+1]
4. Memoize on (l, r) since each subproblem is fully defined by its window
   There are O(N^2) unique windows, each scanning N indices → O(N^3) total
"""
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # pad out-of-bounds with 1 so boundary neighbors are always valid
        nums = [1] + nums + [1]
        
        dp = dict()
        def helper(l, r):
            if l > r:
                # empty window, no balloons left
                return 0
            if (l, r) in dp:
                # return memoized
                return dp[(l, r)]

            max_coins = 0
            for i in range(l, r + 1):
                # burst everything to the left of i before i pops
                coins = helper(l, i - 1)
                # burst everything to the right of i before i pops
                coins += helper(i + 1, r)
                # i is the last balloon to burst in window [l, r]
                # so its only neighbors are the window boundaries
                coins += nums[l - 1] * nums[i] * nums[r + 1]
                max_coins = max(max_coins, coins)

            # memoize and return
            dp[(l, r)] = max_coins
            return max_coins

        return helper(1, len(nums) - 2)