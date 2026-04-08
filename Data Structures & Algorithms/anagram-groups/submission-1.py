class Solution:
    # o(n * m)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # big giveaway: constraint is only lowercase eng letters!
        # each string can generate a hash using its characters
        # put the strings with the same hash in the same sublist

        # o(n) is the number of indices in strs
        # defaultdict gives us empty list when key DNE
        final_map = defaultdict(list)
        for str_i in strs:
            hash_str = self.hash_func(str_i)
            final_map[hash_str].append(str_i)
        
        return list(final_map.values())

    # o(m) where m is the longest string 
    def hash_func(self, s):
        # list of size 26 with 0 default value
        # [1 0 0 0 ....]
        # ord function -> gives ascii value of a char
        # "a" -> 65 , "b" -> 66
        # ord(c) - ord("a")
        ascii_l = [0] * 26
        for ch in s:
            ind = ord(ch) - ord('a')
            ascii_l[ind] += 1

        # list is not hashable in python
        # for some reason tuple is hashable
        return tuple(ascii_l)
