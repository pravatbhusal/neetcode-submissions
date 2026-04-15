class Solution:
    """
    create a dictionary that maps each digit to a list of characters
    then recursively build each possible combination.
    """
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        letters_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        combo = []
        def recurse(i):
            if i >= len(digits):
                if combo:
                    result.append("".join(combo.copy()))
                return
            digit_letters = letters_map[digits[i]]
            for letter in digit_letters:
                # add this digit's letter
                combo.append(letter)
                recurse(i + 1)
                # remove this digit's letter
                # next iteration will use the next digit's letter
                combo.pop()
        
        recurse(0)
        return result