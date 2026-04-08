# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # the hard part is that it's a singly linked list
        # since the array looks like [0, n-1, 1, n-2]
        # split list in the middle, reverse the second half, and merge
        middle = self.getMiddle(head)

        # reverse second half and return head of reverse
        second_head = self.reverse(middle.next)

        # to prevent circular linked list, break the middle's next
        middle.next = None

        # now merge head and second_head
        while second_head:
            tmp1, tmp2 = head.next, second_head.next
            # merge [0, n-1, 1]
            head.next = second_head # [0, n - 1]
            second_head.next = tmp1 # [n - 1, 1]
            # continue
            head, second_head = tmp1, tmp2

    # to find the middle, have slow (+= 1) and fast (+= 2) ptrs.
    def getMiddle(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow ptr is at the middle of the list
        return slow

    # reverse linked list by reversing each link individually
    def reverse(self, head):
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
