"""
To maximize the largest rectangle, left bar must be the largest height.
We create a stack of the open left-bars that haven't found their right bar.
When we encounter a right bar height less than the stack's top (tallest left bar),
pop from the stack and calculate the area between those two bars.

area = (right_i - left_i) * left_height

Example: heights = [7,1,7,2,2,4], answer = 8
Because the heights 7, 2, 2, 4 collapse to height = 2, width = 4.

Create a monotonically increasing stack. The stack pushes (height, i) tuples
of left bars that are still open and not yet found their right bar.

Solution for monotonic increasing stack:
1. If height[i] is greater than top of stack, then push to stack (mono increasing).
2. If height[i] is less than top of stack, then pop and calculate area.
3. After we pop, we push the (height, left_i) because the left bar's index absorbs
the current right bar at i, so we can "extend" the width.
"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []

        max_area = 0
        for i in range(len(heights)):
            left_i = i
            while stack and heights[i] < stack[-1][0]:
                # keep popping left bar till right bar is taller
                left_height, left_i = stack.pop()
                area = (i - left_i) * left_height
                max_area = max(area, max_area)
            
            # push taller right bar and absorb left bar's index (extend width)
            stack.append((heights[i], left_i))

        # no right bar found for the remaining left bars in the stack
        # calculate area using the length of the list as the right bar
        while stack:
            left_height, left_i = stack.pop()
            area = (len(heights) - left_i) * left_height
            max_area = max(area, max_area)
        
        return max_area