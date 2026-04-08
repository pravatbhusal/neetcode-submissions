# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # the huge learning i made here was that a dummy node as head would solve null edge case
        # neetcode says that dummy node is a common technique to avoid null edge case!!
        dummy = ListNode()
        node = dummy

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        
        # merge the remaining items from either list
        node.next = list1 or list2

        # return head
        return dummy.next
    
    # this is my custom solution that's a lot longer and considers too many null edge cases
    # i did not even complete the problem due to how unmaintainble it was
    def mergeTwoListsMySolution(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # this is the merge operation from merge sort
        # time & space: O(N + M) where N = list1 and M = list2

        # this is a sorted list, so i'm thinking two pointers
        # compare the ptr is less than for list1, then move right. and vice versa.
        head = None
        cur = None
        l1_ptr = list1
        l2_ptr = list2
        while l1_ptr is not None and l2_ptr is not None:
            if l1_ptr.val < l2_ptr.val:
                if not cur:
                    # initialize curr, [l1, l2]
                    cur = ListNode(l1_ptr.val)
                    cur.next = ListNode(l2_ptr.val)
                    head = cur
                    cur = cur.next
                else:
                    # [l1, l2]
                    cur.next = ListNode(l1_ptr.val)
                    cur.next.next = ListNode(l2_ptr.val)
                    cur = cur.next.next
            else:
                if not cur:
                    # initialize curr, [l2, l1]
                    cur = ListNode(l2_ptr.val)
                    cur.next = ListNode(l1_ptr.val)
                    head = cur
                    cur = cur.next
                else:
                    # [l2, l1]
                    cur.next = ListNode(l2_ptr.val)
                    cur.next.next = ListNode(l1_ptr.val)
                    cur = cur.next.next
            l1_ptr = l1_ptr.next
            l2_ptr = l2_ptr.next

        # starting from the head, backfill the remaining items
        rem_list = l1_ptr if l1_ptr else l2_ptr
        prev = None
        cur = head
        while rem_list:
            if rem_list.val < cur.val:
                # TODO: backfill to the same ptr as cur
                continue
            else:
                # TODO: backfill to the next ptr of cur
                continue
        return head
