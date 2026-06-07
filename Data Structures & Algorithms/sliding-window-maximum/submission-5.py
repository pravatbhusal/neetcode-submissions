"""
Brute-force: For each window k, get the max() in that window of nums.
How can we optimize getting the max() in the window in O(1) time?

Initial idea: As we slide the window right, we check if the new element is larger than the
current max. If it is, then update the new current max.
WRONG: If the current max slides out of the window, then need to re-get the max.

Build a monotonic decreasing list of alternatives when the current max leaves the window.
To get true O(1), we can use a LinkedList:
1. Pop out the max when it leaves, use a tuple of (value, index)
2. Push in new values when we slide the window to the right

The hard part is ensuring ordering as we add new items. The deque can maintain
only elements that are within the window and index is after smaller elements.

For example, if deque = [5, 3, 1] and num = 4 then pop out 3 and 1.
This is because 4 is greater and guaranteed to be in an index after 3 and 1.
"""
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        result = []
        for i, num in enumerate(nums):
            # pop out smaller than num from queue (monotonic decreasing)
            while queue and queue[-1][0] < num:
                queue.pop()
        
            # slide window to right
            queue.append((num, i))

            # evict old max when it slides out of window
            left = i - k + 1
            if queue[0][1] < left:
                queue.popleft()

            # record max for this window
            if left >= 0:
                result.append(queue[0][0])

        return result