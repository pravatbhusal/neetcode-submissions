class Solution:
    """
    More intuitive solution is have a double for loop that starts a recursive
    search at index (i, j) that looks for the adjacent word.

    There are 4 directions in our backtracking solution: right, left, up, down
    If (i, j) is the target char, then continue. Otherwise return False.

    To not repeat the same path in our backtracking, we need to store the path
    we've visited so far in a set.
    """
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        visited = set()
        def recurse(r, c, word_i):
            if word_i == len(word):
                # found matching word!
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols:
                # out of bounds
                return False
            path = (r, c)
            if path in visited:
                # duplicate path
                return False
            if board[r][c] != word[word_i]:
                # non-matching index
                return False

            # at this point we're at a matching index of word
            # visit all 4 directions to find the next matching adjacent index
            visited.add(path)
            found = (recurse(r + 1, c, word_i + 1) or
                    recurse(r - 1, c, word_i + 1) or
                    recurse(r, c + 1, word_i + 1) or
                    recurse(r, c - 1, word_i + 1))
            visited.remove(path)
            return found

        for r in range(rows):
            for c in range(cols):
                if recurse(r, c, 0):
                    return True
        return False
    
    """
    WRONG: This solution was my original thought, but this is wrong because we're skipping chars
    using .pop(), but the word must be formed using adjacent characters.

    We can only decide to go vertically or horizontally within the board.
    There are 2 directions in our backtracking solution:
    Starting from (0, 0):
    - Go right with char or without char
    - Go down with char or without char

    If we detect that the word is built, then short-circuit return True.
    If not, then continue the recursion until all combinations are checked.

    For example, given:
    A B C
    S F G
    Code might "find" AC by taking A, skipping B, then taking...
    but A and C aren't adjacent, so this is invalid.
    """
    def exist_WRONG(self, board: List[List[str]], word: str) -> bool:
        found = False
        stack = []

        def recurse(i, j):
            if len(stack) and stack[0] == 'B':
                print(stack)
            nonlocal found
            if found:
                # short-circuit, found solution
                return True
            if "".join(stack) == word:
                # found word
                found = True
                return True
            if i >= len(board) or i < 0:
                # out of bounds
                return False
            if j >= len(board[i]) or j < 0:
                # out of bounds
                return False

            # add char and go right
            char = board[i][j]
            stack.append(char)
            recurse(i + 1, j)

            # without char go right
            stack.pop()
            recurse(i + 1, j)

            # add char and down
            stack.append(char)
            recurse(i, j + 1)

            # without char go down
            stack.pop()
            recurse(i, j + 1)

        recurse(0, 0)
        return found