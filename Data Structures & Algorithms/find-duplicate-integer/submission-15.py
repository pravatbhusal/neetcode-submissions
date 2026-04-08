class Solution:
    """
    Similar problem: "Linked List Cycle"

    We can use fast and slow pointers.
        - fast = fast.next.next
        - slow = slow.next
    
    If we detect fast == slow, then there exists a cycle.
    
    We can take advantage of the indices because nums[i] < len(nums)
    So think of the fast/slow ptrs as ptrs of a cyclical linked list.
    And we're trying to find the ptr where the cycle begins (duplicate number).
    """
    def findDuplicate(self, nums: List[int]) -> int:
        # First detect the intersection (collision) of fast and slow ptr
        # fast moves 2x faster on the linked list
        # slow moves 1x fast on the linked list
        fast = 0
        slow = 0
        while True:
            fast = nums[nums[fast]] # 2x faster
            slow = nums[slow]
            if slow == fast:
                # found intersection point
                break

        # there's an equal distance between index 0 and the intersection till it meets the cycle
        # so iterate incrementally +1 till both ptrs meet, which is where the cycle is
        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow2 == slow:
                # found cycle, return the num
                return slow2