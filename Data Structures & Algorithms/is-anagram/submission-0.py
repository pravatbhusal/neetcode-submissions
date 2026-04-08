class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = dict()
        t_dict = dict()

        # add all strings from s to s_dict
        for s_str in s:
            if s_str in s_dict:
                s_dict[s_str] += 1
            else:
                s_dict[s_str] = 1

        # add strings from t to t_dict
        for t_str in t:
            if t_str in t_dict:
                t_dict[t_str] += 1
            else:
                t_dict[t_str] = 1

        # "==" operator in python compares the keys/values
        # python uses "is" operator comparing references
        return s_dict == t_dict
            