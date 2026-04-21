"""
Similar solution to implement Trie (prefix tree). We need to mark each char node
with is_word in our trie if it's the last letter of a word.

The wildcard is that "." can be matched with any letter. This means the search
would recursively check all branches for a "." char.
"""
class Node:
    def __init__(self, char: str, children: dict, is_word: bool):
        self.char = char
        self.children = dict()
        self.is_word = is_word

class WordDictionary:

    def __init__(self):
        self.root = Node(None, dict(), None)

    def addWord(self, word: str) -> None:
        cur = self.root
        for i in range(len(word)):
            char = word[i]
            if char not in cur.children:
                cur.children[char] = Node(char, dict(), False)
            char_n = cur.children[char]
            if i == len(word) - 1:
                char_n.is_word = True
            cur = char_n

    def search(self, word: str) -> bool:
        def helper(word, cur):
            for i in range(len(word)):
                char = word[i]
                if char == ".":
                    # wildcard, recursively check all possible char paths
                    for node in cur.children.values():
                        found = helper(word[i+1:], node)
                        if found:
                            return True
                if char not in cur.children:
                    return False
                cur = cur.children[char]
            return cur.is_word
        cur = self.root
        return helper(word, cur)
