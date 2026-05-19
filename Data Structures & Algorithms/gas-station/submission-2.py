"""
gas[i] = add total gas
cost[i] = subtract total gas
Return the gas[i] index to start the circular route without running out of gas.

Brute-force O(N^2): Check every index and seeing if it completes the circuit.

Let's conceptualize this using an example:
gas =  [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
diff = [-2, -2, -2, 3, 3]

I'm thinking the result is the index that has the maximal diff that is also
before other positive value indices. In the above example, that result is at
index 4 because its value is 3 and is before the positive value in index 5.

The greedy formula we can use is sum(gas) >= sum(cost) because that ensures
we have enough gas to complete the circuit. We can keep track of a running sum
of diff and ensure it never goes negative (ran out of gas). If your running total
goes negative at index i, every index from your current start up to i is eliminated
as a valid starting point because our current start couldn't sustain itself to i.

This is very similar to Kadane's algorithm.
"""
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total = 0
        start = 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff

            if total < 0:
                # negative gas tank, reset
                # all prev indices were invalid
                total = 0
                start = i + 1

        return start