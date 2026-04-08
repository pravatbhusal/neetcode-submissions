"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

"""
Each node contains a "random" pointer to another random node.

For each node, the deep copy needs:
1. val
2. next pointer to the next deep copied node
3. a random pointer to the random deep copied node

The reason this is hard is because how can we ensure that we point to the correct random deep copied node?
It's randomly all over the place so there's no sequence to storing it. It's unordered.

Solution: Create a dict with key as the original node ref and the value as the deep copied node ref.
Hard part is how do we update ref of the deep copy to also not point to the original node?
We need to store the ref of the original node so that when we iterate the list and we encounter
on the second pass the ref again, we update the pointers of that ref to the deep copy.
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        copies = defaultdict(None)

        # fill copies with original ref as key and the shallow copied node
        cur = head
        while cur:
            copy = Node(cur.val, None, None)
            copies[cur] = copy
            cur = cur.next

        # second pass now that all refs are stored we can set the pointers to the copied node
        cur = head
        while cur:
            copies[cur].next = copies.get(cur.next)
            copies[cur].random = copies.get(cur.random)
            cur = cur.next

        return copies[head]