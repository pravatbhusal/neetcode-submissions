"""
Keep track of the largest heights of the two ptrs to maximize the area of water.

To get the water area, we get the min of those two ptrs to find the water that can
be trapped in the bucket. Then subtract the "space" (height) the bucket takes up.

Running sum: max(0, min(max_left, max_right) - height[ptr])

The hard-part is the condition when to move left and right ptr. We move the
ptr that is smaller so that we keep the maximal ptr on the other side.
This guarantees that whichever side we calculate, the OTHER side's wall is
already tall enough.

This solution calculates the rain water split in two halves: left and right.
The max_left is the max height so far on the left-side (left ptr).
The max_right is the max height so far on the right-side (right ptr).

When we process left-side, running sum collapses to: max_left - height[left]
When we process right-side, running sum collapses to: max_right - height[right]
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_left, max_right = height[left], height[right]

        sum = 0
        while left < right:
            if height[left] < height[right]:
                # move left ptr
                left += 1
                # running sum from left-side
                max_left = max(height[left], max_left)
                sum += max_left - height[left]
            else:
                # move right ptr
                right -= 1
                # running sum from right-side
                max_right = max(height[right], max_right)
                sum += max_right - height[right]

        return sum
