# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        # one pass O(N), flip two pointers (prev and curr)
        prev = None
        curr = head

        while curr:
            # flip
            temp = curr.next
            curr.next = prev

            # move to next
            prev = curr
            curr = temp

        return prev