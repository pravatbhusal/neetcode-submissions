# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # iterate the list until tail to get the length of the list, O(N)
        # re-iterate the list until finding n, O(N)
        # unlink the node from the prev
        length = self.get_length(head)
        stop = length - n

        # get the node prev before n and the node at n
        i = 0
        cur = head
        prev = None
        while i < stop:
            prev = cur
            cur = cur.next
            i += 1

        if not prev:
            # edge case, deleting head node
            return head.next

        # delink at n
        if prev and cur:
            prev.next = cur.next
        elif prev:
            prev.next = None
        return head

    def get_length(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length