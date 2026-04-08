class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            # s1 bigger than s2, so impossible permutation
            return False

        # store the freq of chars of s1 in a dict
        # when we encounter a char in s2 in s1, start sliding window
        # if window len == s1 and has same count of chars as s1, return True

        s1_f = Counter(s1)
        window = Counter()
        window_size = 0
        for i, char in enumerate(s2):
            if char in s1_f:
                window[char] += 1
                window_size += 1
            else:
                # reset window
                window = Counter()
                window_size = 0

            if window_size > len(s1):
                # window too large, remove first element from window
                left = s2[i - len(s1)]
                window[left] -= 1
                window_size -= 1
                if window[left] == 0:
                    # must explicitly delete key in Counter
                    del window[left]
            
            if window == s1_f:
                return True

        return False

