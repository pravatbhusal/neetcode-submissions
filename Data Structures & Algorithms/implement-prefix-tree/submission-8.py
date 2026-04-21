class Node:
    def __init__(self, char: str, children: dict, is_word: bool):
        self.char = char
        self.children = dict()
        self.is_word = is_word

class PrefixTree:

    def __init__(self):
        self.root = Node(None, dict(), False)

    def insert(self, word: str) -> None:
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
        cur = self.root
        for i in range(len(word)):
            char = word[i]
            if char not in cur.children:
                return False
            cur = cur.children[char]
            if i == len(word) - 1:
                return cur.is_word
        return False

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for i in range(len(prefix)):
            char = prefix[i]
            if char not in cur.children:
                return False
            cur = cur.children[char]
            if i == len(prefix) - 1:
                return True
        return False
