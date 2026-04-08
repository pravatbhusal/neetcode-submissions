class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # pick two ptrs and square (^2) the smallest of the two ptrs
        # naive solution O(N^2) with double for loop
        # left ptr (0 index), right ptr (end index)
        left = 0
        right = len(heights) - 1

        max_area = 0
        while left < right:
            length = right - left
            height = (heights[left] if heights[left] < heights[right] else heights[right])
            area = length * height

            if area > max_area:
                max_area = area

            if heights[left] < heights[right]:
                # left is too small, so go to next index
                left += 1
            else:
                # right is too small, so go to next index
                right -= 1

        return max_area