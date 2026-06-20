"""
The problem asks us to find the increasing order from a given sorted words list.
Using the words list, find which letter is an edge to another letter and build an adjacency list.

Run topological sort on the letter dependency graph and return the output of the sort.
If there's a cycle (cannot visit all nodes) then the arrangement is incorrect so return "".

The hard part is building the adjacency list from the words list. How can we know which letter has an edge to another?

As mentioned the 1st rule "the first letter where they differ is smaller in word a than word b"
We can do this by comparing the index of the first non-matching letter amongst adjacent words.
Ex: ["wrt", "wrf", "er", "ett", "rftt"]
t -> f
w -> e
r -> t
e -> r

There's also the 2nd rule of a being prefix of b. We can check that when building adjacency list.
Ex: ["abc", "ab"] - "ab" is after "abc" but it's a prefix so that means this list is invalid
"""
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # build adjacency list using 
        adj = {c: set() for w in words for c in w}
        for i in range(1, len(words)):
            w1, w2 = words[i - 1], words[i]
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                # w2 is prefix of w1, but it's after in words list (invalid rule 2)
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    # found first non-matching letter
                    # add edge w1[j] -> w2[j]
                    adj[w1[j]].add(w2[j])
                    break
        
        order = []
        visited, cycle = set(), set()
        def dfs(letter):
            if letter in cycle:
                # cycle detected
                return True
            if letter in visited:
                # already processed
                return False

            # visit the neighbor of this letter
            cycle.add(letter)
            for neighbor in adj[letter]:
                if dfs(neighbor):
                    return True

            cycle.remove(letter)
            visited.add(letter)
            order.append(letter)

        for letter in adj.keys():
            if dfs(letter):
                # cycle detected
                return ""

        # return topological sort order
        order.reverse()
        return "".join(order)