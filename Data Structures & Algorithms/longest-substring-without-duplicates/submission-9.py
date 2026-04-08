class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        # two pointers where you check for sequence of non-repeating chars
        left = 0
        right = 0

        substr = set()
        longest = 0
        while right < len(s):
            if s[right] not in substr:
                # add char into the substr set
                substr.add(s[right])
                right += 1
            else:
                # restart substr
                # remove left char and restart substr set
                substr.remove(s[left])
                left += 1
            if len(substr) > longest:
                longest = len(substr)
        return longest
