"""
Brute-force O(W * N * M * 4L): For each word, find the starting letter of the word on
the board then start DFS traversing to check each letter exists.

Optimal Trie solution O(N * M * 4L): Add each word into a Trie and mark the final
letter of a word with "is_word: True". Then DFS starting at every cell of the board
and the moment a path no longer is a valid prefix in the Trie, backtrack.

To mark a cell as visited, use "#". Then on backtrack revert it back.
"""

class TrieNode:
    def __init__(self):
        self.children = dict()
        self.word_i = -1

    def addWord(self, word, i):
        cur = self
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        
        # store word's index in the last letter node, marking as "is word"
        # useful as a ref when indexing the words list
        cur.word_i = i

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # populate words to Trie
        root = TrieNode()
        for i in range(len(words)):
            root.addWord(words[i], i)

        ROWS = len(board)
        COLS = len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        self.result = list()
        def dfs(r, c, node):
            if r not in range(ROWS) or c not in range(COLS):
                # out of bounds
                return
            
            letter = board[r][c]
            if letter not in node.children:
                # letter not found in Trie, remove it to not come back here
                return
            
            prev = node
            node = node.children[letter]
            if node.word_i != -1:
                # found word!
                self.result.append(words[node.word_i])
                node.word_i = -1
                if len(node.children) == 0:
                    # prune this empty word node (to not revisit it)
                    del prev.children[letter]
                    return
            
            # mark as visited, then recurse each direction
            board[r][c] = "#"
            for dir in directions:
                dfs(r + dir[0], c + dir[1], node)
            # unmark (backtrack)
            board[r][c] = letter

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)
        return self.result
