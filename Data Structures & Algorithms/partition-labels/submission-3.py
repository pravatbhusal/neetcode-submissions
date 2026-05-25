"""
Maximize the number of substrings while ensuring that a letter appears
in only one substring.

Greedy solution:
If we know all chars of a substr will never appear again if we iterate any
further on string s, then we can break that substr. To do this, we need
to map each char of s to the last index.
"""
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # map of each char's last index
        lasts = dict()
        for i, char in enumerate(s):
            lasts[char] = i

        # substr variables
        substr = set()
        size = 0
        lasts_count = 0

        result = []
        for i, char in enumerate(s):
            substr.add(char)
            size += 1

            # is this the last index of this char?
            last_i = lasts[char]
            if i == last_i:
                # last index, satisfied this last char for this substr
                lasts_count += 1

            # did we find all last chars for this substr?
            if lasts_count == len(substr):
                # break substring
                result.append(size)
                substr = set()
                size = 0
                lasts_count = 0
        
        return result