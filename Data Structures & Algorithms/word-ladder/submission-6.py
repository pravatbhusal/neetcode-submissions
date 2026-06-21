"""
I can transform a word into another word if only 1 character at the same index differs between the two words.
We can build an adjacency list of a word that can be transformed into other word(s). This builds a graph where there
exists an edge word1 -> word2 if word1 can be transformed into word2.

Building the adjacency list:
How can we efficiently build an adjacency list by comparing two words can be transformed?
We can store each pattern of a word into a set then compare that the current word doesn't exist in set.
Ex: "bat" -> "*at", "b*t", "ba*" then compare "bag" and we would see "ba*" exists in this set.
This is O(N * M^2) where N = len of wordList and M = length of word.
This is because we need to modify the string at index and check each combination.

Shortest-path algorithm (BFS):
To return the minimum number of words from beginWord -> endWord, find the shortest path on the graph.
This is an unweighted graph, so the shortest path is found using standard BFS.
"""
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # build patterns that maps pattern -> words that match
        patterns = defaultdict(set)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                patterns[pattern].add(word)

        # run BFS to find shortest path from beginWord -> endWord
        result = 0
        queue = deque([beginWord])
        while queue:
            result += 1
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    # found path!
                    return result
                # seed next words in graph
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]
                    queue.extend(patterns[pattern])
                    del patterns[pattern]
        
        # no path found
        return 0