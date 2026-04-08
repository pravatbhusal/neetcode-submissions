class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.orderNComplexity(s, t)

    # O(N) time and space
    def orderNComplexity(self, s: str, t: str):
        if len(s) != len(t):
            return False

        # count chars in s
        s_dict = dict()
        for s_char in s:
            s_char_count = s_dict.get(s_char, 0)
            s_dict[s_char] = s_char_count + 1

        # count chars in t
        t_dict = dict()
        for t_char in t:
            t_char_count = t_dict.get(t_char, 0)
            t_dict[t_char] = t_char_count + 1

        return s_dict == t_dict
            