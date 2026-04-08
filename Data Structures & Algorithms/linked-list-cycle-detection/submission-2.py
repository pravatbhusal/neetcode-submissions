# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
We can solve the cycle problem is if we used fast and slow pointers.
    - fast = fast.next.next
    - slow = slow.next
    
If a cycle did exist, fast would end up looping back and then fast == slow.
"""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        fast = head.next
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                # fast looped back, and now points back to slow
                return True
        return False
