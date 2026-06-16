# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Similar Problem: "Reverse Linked List"
This is a very similar problem, but we only reverse k nodes in the list at a time.

O(N/k) space solution (my idea): Split the list into sections of k length, and each section will be reversed.
Store the head of each section, then merge each sections into a single list.

O(N/k) space recursive solution: Reverse the first k nodes, then recurse on the remaining list, and repeat.
The recursive call returns the new head of the next reversed group, which we attach to the tail of the current group.
O(N/k) space because we are making a recursive call for each group of k nodes.

O(1) space iterative solution (optimal): Same logic as the recursive solution but avoids O(N/k) call stack space.
Instead of the call stack implicitly tracking each group's tail, we explicitly track the previous group's tail using
a prev_tail pointer, connecting it forward to the current group's new head as we go.

Iterative Example:

dummy → 1 → 2 → 3 → 4 → 5,  k=2

After reversing [1,2]:
dummy    2 → 1    3 → 4 → 5

Wire dummy → 2:   dummy → 2 → 1    3 → 4 → 5
Wire 1 → 3:       dummy → 2 → 1 → 3 → 4 → 5
prev_tail = 1

After reversing [3,4]:
dummy → 2 → 1    4 → 3    5

Wire 1 → 4:       dummy → 2 → 1 → 4 → 3    5
Wire 3 → 5:       dummy → 2 → 1 → 4 → 3 → 5
prev_tail = 3
"""
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # dummy node to store head ref
        dummy = ListNode(0)
        dummy.next = head
        prev_tail = dummy

        while True:
            # get kth node of this group
            kth = self.getKthNode(prev_tail, k)
            if not kth:
                break

            # reverse k node group (Reverse Linked List LC #206)
            next_kth_group_head = kth.next
            kth_group_head = prev_tail.next
            prev, cur = prev_tail, prev_tail.next
            while cur != next_kth_group_head:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp

            # wire prev_tail to new head of reversed group
            prev_tail.next = prev
            prev_tail = kth_group_head

            # wire tail (old head) to next group
            kth_group_head.next = next_kth_group_head

        # return head
        return dummy.next

    def getKthNode(self, cur, k):
        while cur and k > 0:
            cur = cur.next
            k -= 1
        return cur