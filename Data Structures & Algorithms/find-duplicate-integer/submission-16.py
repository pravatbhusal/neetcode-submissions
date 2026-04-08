class Solution:
    """
    Similar problem: "Linked List Cycle"

    We can use fast and slow pointers.
        - fast = fast.next.next
        - slow = slow.next
    
    If we detect fast == slow, then there exists a cycle.
    
    We can take advantage of the indices because nums[i] < len(nums)
    So think of the values as ptrs of a linked list.
    And we're trying to find the ptr where the cycle begins (duplicate number).
    """
    def findDuplicate(self, nums: List[int]) -> int:
        # First detect the intersection (collision) of fast and slow ptr
        # fast moves 2x speed on the linked list
        # slow moves 1x speed on the linked list
        fast = 0
        slow = 0
        while True:
            fast = nums[nums[fast]] # move 2x speed
            slow = nums[slow] # move 1x speed
            if slow == fast:
                # found intersection point
                break

        # there's an equal distance between index 0 and the intersection to encounter the cycle
        # so iterate incrementally till both ptrs meet, which is where the cycle is
        slow2 = 0
        while True:
            slow2 = nums[slow2] # move 1x speed
            slow = nums[slow] # move 1x speed
            if slow2 == slow:
                # found cycle, which is the duplicate
                return slow2