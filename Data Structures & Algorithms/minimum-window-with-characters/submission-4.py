"""
Similar Problem: "Permutation in String" (PiS)
The above problem was finding if characters of a substring exists in a string.

This problem asks to find the smallest substring in s that has all chars of t.
This is a sliding window since we're finding a "window" (substring) in s.
Use a Counter of t to ensure we satisfy all chars of t in a window.

What two conditions expand (right += 1) and shrink (left -= 1) the window?
In the PiS problem, we expanded when we encountered a new char that matched.
Then we reset the entire window when a char did not match.

For this problem, we need to expand when we encounter a new char for sure.
But when do we shrink? If we have too many chars, shrink as much as possible
while the window is still valid substring of t. This greedily gets us the
smallest possible window.

Like in PiS problem, we could check if window is valid by checking the
window == Counter(t), but the window may not have chars from t so it's
difficult to do an exact comparision.

We have two variables to determine if window is satisfied:
- need = number of unique chars we need to satisfy the window of t
- have = counter tracking do we have all the chars with freq in window?
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_chars = Counter(t)
        need = len(t_chars)

        left = 0
        have = 0
        window_size = math.inf
        min_window = s
        window = Counter()
        for right, right_char in enumerate(s):
            # always expand window right
            window[right_char] += 1

            if window[right_char] == t_chars[right_char]:
                # satisfied this char for the window
                have += 1

            # minimize window while it's still satisfied
            while have == need:
                # record minimum window
                window_size = right - left + 1
                if window_size < len(min_window):
                    min_window = s[left:right+1]

                # shrink from left
                left_char = s[left]
                window[left_char] -= 1
                left += 1

                # are we still satisfied?
                if window[left_char] < t_chars[left_char]:
                    have -= 1

        return min_window if window_size != math.inf else ""