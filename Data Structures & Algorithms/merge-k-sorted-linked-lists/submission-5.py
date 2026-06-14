# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Similar Problem: Merge two Sorted Lists

If we ran the Merge function on k lists, the time complexity is O(N*k)
This is inefficient because a sequential loop (k times) would re-process
the same already-merged nodes over and over which is repeated work.

Instead, we can solve it like a Merge Sort O(N*log(k)) using divide and conquer.
Merge sort's Divide and conquer algorithm:

While len(lists) > 1: - O(log2(K))
    For each two lists (a and b), merge them together - O(N)

This reduces the problem space by / 2 each time, which is Olog2(k), because
we keep merging two sorted lists on each while loop iteration.

Divide and conquer visualization:

list1  list2   list3  list4
   \   /          \   /
  merged12      merged34
        \         /
       merged1234
"""
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists) > 1:
            merged = []
            # divide problem space by 2
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                # conquer (merge) two lists
                merged.append(self.merge(l1, l2))
            lists = merged
        
        return lists[0]

    def merge(self, l1, l2):
        dummy = ListNode()
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                # merge l1's node
                cur.next = l1
                l1 = l1.next
            else:
                # merge l2's node
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        # backfill remaining elements
        cur.next = l1 or l2

        # return head
        return dummy.next