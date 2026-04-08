class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return self.hash_solution(strs)

    # hash each word by letter, put matching hashes in the same sublist
    # word is lowercase English, so we can use an alpha ascii map
    # each word with the same ascii map (hash) are put in the same sublist
    def hash_solution(self, strs):
        word_dict = defaultdict(list)
        for word in strs:
            letters = [0] * 26
            for char in word:
                char_i = ord(char) - ord('a')
                letters[char_i] += 1
            # tuple is hashable because it's immutable
            letters_hash = tuple(letters)
            word_dict[letters_hash].append(word)
        return list(word_dict.values())
