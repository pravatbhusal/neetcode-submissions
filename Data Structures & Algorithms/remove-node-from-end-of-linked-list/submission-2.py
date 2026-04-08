# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None:
            return 0

        # handle simple case of only 1 item in list
        if head.next == None:
            return None

        # keep iterating until encountering the head again
        list_len = 1
        cur = head.next
        while cur != None:
            cur = cur.next
            list_len += 1
        
        # we need to delete the node at list_len - n
        delete_n = list_len - n

        # delete the first item from list
        if delete_n == 0:
            return head.next

        # keep iterating until we hit right before delete_n
        i = 0
        cur = head
        while i != delete_n - 1:
            cur = cur.next
            i += 1
        
        # dereference the node by setting the next of the next
        cur.next = cur.next.next

        # return the start of the list (head)
        return head
