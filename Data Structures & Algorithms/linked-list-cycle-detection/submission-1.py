# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # do it in O(N) time somehow
        # we can prob store "seen" nodes? this would be O(N) space tho
        # O(1) space, so like 2 ptrs? NOPE
        # a good idea is to just mark each visited node!
        # re-use val to prevent allocating space for a new variable

        # constraint makes it not less than -1000, so use -1001 as visited
        visited = -1001
        cur = head
        while cur:
            if cur.val == visited:
                return True
            cur.val = visited
            cur = cur.next
        return False
