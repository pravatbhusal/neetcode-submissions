"""
Similar Problem: "Number of 1 Bits"
We use the same intuition to count the number of 1-bits for each [0, n].

The operation to count 1-bits is O(1).
Then perform counting on range(n), so solution would be O(N) time.
"""
class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n + 1):
            count = self.hammingWeight(i)
            result.append(count)
        return result
    
    def hammingWeight(self, n: int) -> int:
        res = 0
        for i in range(32):
            mask = 1 << i
            if mask & n:
                # 1-bit exists on i
                res += 1
        return res