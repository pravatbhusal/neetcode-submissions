"""
Similar Problem: "Number of 1 Bits"

O(log(N)) solution:
Similar to "Number of 1 Bits" problem use same solution to count number of 1s.
Then perform counting on range(n) where n is a 32 bit integer. In reality,
we need to consider the count as actually O(log(n)) because log2(2^31) = 32.
So real complexity is O(Nlog(N)).



"""
class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n + 1):
            count = self.hammingWeight(i)
            result.append(count)
        return result
    
    # Solution from "Number of 1 Bits" problem
    def hammingWeight(self, n: int) -> int:
        res = 0
        for i in range(32):
            mask = 1 << i
            if mask & n:
                # 1-bit exists on i
                res += 1
        return res