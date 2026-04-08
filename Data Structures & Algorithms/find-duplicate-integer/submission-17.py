class Solution:
    """
    Similar problem: "Linked List Cycle"

    We can use fast and slow pointers.
        - fast = fast.next.next
        - slow = slow.next


    In the Linked Problem cycle problem, if we detect fast == slow, then there exists a cycle.
    The Linked List cycle problem was easy to solve because it just returned a boolean True/False
    if there existed a cycle in the list. But this problem is harder because we need to detect
    where the cycle exists.
    
    We can take advantage of the values because nums[i] < len(nums), so think of the values as ptrs of a linked list.
    And we're trying to find the ptr where the cycle begins (duplicate number).

    Phase 1: Find the distance of the cycle, which can be done by finding intersection point.
    Phase 2: Find where the cycle is
    """
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: First detect the intersection (collision) of fast and slow ptr
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

        # There's an equal distance between index 0 and the intersection point to the cycle
        # Phase 2: iterate incrementally till both ptrs meet, which is where the cycle is
        slow2 = 0
        while True:
            slow2 = nums[slow2] # move 1x speed
            slow = nums[slow] # move 1x speed
            if slow2 == slow:
                # found cycle, which is the duplicate
                return slow2