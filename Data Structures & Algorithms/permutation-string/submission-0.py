class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            # s1 bigger than s2, so impossible permutation
            return False

        # store the freq of chars of s1 in a dict
        # when we encounter a char in s2 in s1, start sliding window
        # if window len == s1 and has same count of chars as s1, return True

        s1_count = Counter(s1)
        window = Counter(s2[:len(s1)])

        if window == s1_count:
            return True

        for i in range(len(s1), len(s2)):
            # Add new char on the right
            window[s2[i]] += 1

            # Remove old char on the left
            left = s2[i - len(s1)]
            window[left] -= 1
            if window[left] == 0:
                del window[left]

            if window == s1_count:
                return True

        return False

