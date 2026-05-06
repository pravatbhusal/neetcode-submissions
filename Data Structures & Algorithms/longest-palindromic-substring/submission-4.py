"""
Similar to "Longest Substring without Repeating Characters" problem, which was solved with sliding window.
The caveat here is that we want to find a palindromic substring. What condition can we slide the window to verify is palindrome?
Well there is no monotonic condition with new the char we add/remove to validate if substr is palindrome, meaning you
can't maintain the "is palindrome" property incrementally. This implies it's not a sliding window problem.

Brute-force solution: Check every substring and check if that substring is a palindrome, O(N^2 * N) = O(N^3).

Efficient solution: Can we use sub-problems of the string?
Example: "ababd"
"a" -> True
"ab" -> False
"ba" -> False
"aba" -> True
"bab" -> True
"abab" - False
"babd" -> False
"ababd" -> False

This is a two-pointers solution (not DP solution). That center is either a single character (odd length) or an adjacent
equal pair (even length). Running both checks at every index guarantees every possible center is tried.

We can do this efficiently by starting the check from the middle char and expand left/right.
Ex: s[2] = "a", so expand to "bab" which is palindrome. Then do that again and expand to "ababd".
This works for odd-number of characters.

Now for the case of even-numbers, such as "abbc".
Ex: s[2] = "b" we can't simply expand to "bbc" it would fail to recognize the palindrome "bb".
So we need a 2nd loop that starts l = i and r = i + 1 so then it would start as "bb".
Then it would expand outwards to "abbc".
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""

        def expand(l, r):
            nonlocal longest
            while l >= 0 and r < len(s) and s[l] == s[r]:
                palin_len = r - l + 1
                if palin_len > len(longest):
                    # update longest palindrome
                    longest = s[l:r+1]
                l -= 1
                r += 1
        
        for i in range(len(s)):
            # odd check
            expand(i, i)
            # even check
            expand(i, i + 1)
        
        return longest
