class Solution:
    """
    Iterate the string s and make substrings. If a substring is a palindrome, then
    recurse on it until we build all possible combintions of that substring's palindrome.
    """
    def partition(self, s: str) -> List[List[str]]:
        result = []

        # partitions sublist for a substring of s
        partitions = []

        def is_palindrome(word):
            r_word = "".join(reversed(word))
            return r_word == word

        def recurse(i):
            if i >= len(s):
                result.append(partitions.copy())
                return
            for j in range(i, len(s)):
                substr_s = s[i:j+1]
                if is_palindrome(substr_s):
                    # substring is palindrome, start recursing for this substring
                    partitions.append(substr_s)
                    recurse(j + 1)
                    partitions.pop()

        recurse(0)
        return result
    
    """
    WRONG solution because this approach builds individual characters, not substrings.
    The check validates the entire partition list as a palindrome rather than filtering
    for partitions where each individual substring is a palindrome.
    
    Brute-force and generate all possible substring combinations.
    Then check each combination is a palindrome.
    """
    def partition_WRONG(self, s: str) -> List[List[str]]:
        result = []

        def is_palindrome(word):
            r_word = list(reversed(word))
            return r_word == word

        sub_s = []
        def recurse(i):
            nonlocal sub_s
            if i >= len(s):
                # check if palindrome
                if is_palindrome(sub_s):
                    result.append(sub_s.copy())
                return

            # add char
            sub_s.append(s[i])
            recurse(i + 1)

            # start new sub list
            sub_s = []

            # remove char
            sub_s.pop()
            recurse(i + 1)

        recurse(0)
        return result
        