"""
Very similar problem to "Longest Palindromic Substring", but difference is that we're counting the number of substrings.
We can use the same concept of expanding from the middle char for both odd and even cases.

This is a two-pointers solution (not DP solution). That center is either a single character (odd length) or an adjacent
equal pair (even length). Running both checks at every index guarantees every possible center is tried.
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def expand(l, r):
            nonlocal count
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # substr is valid palindrome
                palin_len = r - l + 1
                count += 1
                l -= 1
                r += 1
        
        for i in range(len(s)):
            # odd check
            expand(i, i)
            # even check
            expand(i, i + 1)
        
        return count