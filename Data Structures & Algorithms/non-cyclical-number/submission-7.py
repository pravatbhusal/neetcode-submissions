"""
This is a cycle detection problem, which we can solve with either a seen
set or a fast/slow ptr.

O(log(N)) space: Extract each digit using % 10 and // 10 and use a seen set
to store the sum of the squares. Keep looping till sum == 1 or seen sum.

O(1) space: Perform the same calculation as above, but use a fast/slow ptr.
The slow ptr will track the previous sum at 1x speed while the fast ptr will
track the sum at 2x speed. If the slow ptr ever catches up to the fast ptr,
then return False.
"""
class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.sum(n)
        
        while fast != 1:
            if slow == fast:
                # cyclical number
                return False
            slow = self.sum(slow)
            fast = self.sum(self.sum(fast))
        return True

    def sum(self, n):
        sum = 0
        while n >= 1:
            digit = n % 10
            sum += digit ** 2
            n //= 10
        return sum