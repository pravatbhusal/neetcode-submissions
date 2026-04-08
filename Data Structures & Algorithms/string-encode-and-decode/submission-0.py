class Solution:

    def encode(self, strs: List[str]) -> str:
        # every possible char can be in strs list.
        # how can we create a delim?
        # we can use 2 delimeters: len(str) + delim
        enc = ""
        for cur_str in strs:
            encoded = str(len(cur_str)) + "#" + cur_str
            enc += encoded
        return enc

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            # decode the str len
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            # using the length, decode the cur_str
            cur_str = s[j + 1: j + 1 + length]
            res.append(cur_str)
            i = j + 1 + length
        return res