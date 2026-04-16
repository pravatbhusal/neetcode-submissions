class Node:
    def __init__(self, char: str, children: dict, is_word: bool):
        self.char = char
        self.children = dict()
        self.is_word = is_word

class PrefixTree:

    def __init__(self):
        self.root = Node(None, dict(), False)

    def insert(self, word: str) -> None:
        def dfs(cur, i):
            if i >= len(word):
                # base case, done adding chars
                cur.is_word = True
                return
            char = word[i]
            if char not in cur.children:
                cur.children[char] = Node(char, dict(), False)
            dfs(cur.children[char], i + 1)
            
        dfs(self.root, 0)

    def search(self, word: str) -> bool:
        def dfs(cur, i):
            if i >= len(word):
                # base case, check if this node is marked as is_word
                return cur.is_word
            char = word[i]
            node = cur.children.get(char)
            if not node:
                # word does not exist in trie
                return False
            return dfs(node, i + 1)
        
        return dfs(self.root, 0)

    def startsWith(self, prefix: str) -> bool:
        def dfs(cur, i):
            if i >= len(prefix):
                # base case, prefix exists
                return True
            char = prefix[i]
            node = cur.children.get(char)
            if not node:
                # prefix does not exist in trie
                return False
            return dfs(node, i + 1)
        
        return dfs(self.root, 0)
