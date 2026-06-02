"""
Similar Problem: "Number of 1 Bits"

O(log(N)) solution:
Similar to "Number of 1 Bits" problem use same solution to count number of 1s.
Then perform counting on range(n) where n is a 32 bit integer. In reality,
we need to consider the count as actually O(log(n)) because log2(2^31) = 32.
So real complexity is O(Nlog(N)).

O(N) solution:
Use DP and memoize repeated sequence of bits.
Ex: n = 8 becomes
0000 = 0 -> 0 bits
0001 = 1 -> 1 bit
0010 = 2 -> 1 bit
0011 = 3 - > 2 bits
0100 = 4 -> 1 bit
0101 = 5 -> 1 bit
0110 = 6 -> 2 bits
0111 = 7 -> 3 bits
1000 = 8 -> 1 bit

Repeated work is the bit count itself. Ex: 0111 = 7 and this is essentially
adding 1 more bit to 0011 = 3. So how can we know to re-use 3 when i = 7?

Notice that for every power of 2, the binary value has only 1 bit.
We can take advantage of this to make an offset for a DP recurrence.
Recurrence function: dp[i] = 1 + dp[i - offset]
Ex: dp[7] = 1 + dp[7 - 4] = 1 + 2 = 3
"""
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if i / 2 == offset:
                # i is a power of 2
                offset *= 2
            dp[i] = 1 + dp[i - offset]
        return dp
