"""
heights[r][c] = height

Water can flow up, down, left, or right means that we need a directions array.
Water only flows to a neighbor with height equal or lower than itself.

Find the cells that can go BOTH to the top + left and to the bottom + right.

Solution (Inefficient):
For each cell, perform a BFS and check that at each level there is a possible
cell that it can enter. If there's a path that reaches both the top + left and
bottom + right, then that cell is valid.

Solution multi-source BFS (Efficient):
Instead of BFS on each cell, start from the ocean and find cells that flow to it.
This means we find cells with height greater than or equal to the current cell.

We can run BFS on the Pacific ocean cells and another BFS on the Atlantic ocean
cells. Then return the union of the two lists, which are the cells that can go
to both the Pacific and Atlantic oceans.
"""
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if len(heights) == 0:
            return []

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(start):
            flowables = set(start)
            queue = deque(flowables)

            while queue:
                cell = queue.popleft()
                row, col = cell
                for dir in directions:
                    n_row, n_col = row + dir[0], col + dir[1]
                    in_bounds = n_row in range(len(heights)) and n_col in range(len(heights[0]))
                    if in_bounds:
                        # >= check because source is from ocean
                        can_flow = heights[n_row][n_col] >= heights[row][col]
                        cell = (n_row, n_col)
                        if can_flow and cell not in flowables:
                            # water can flow from this cell
                            flowables.add(cell)
                            queue.append(cell)
            return flowables

        # cells starting from pacific ocean
        pacifics = set()
        for i in range(len(heights[0])):
            pacifics.add((0, i))
        for i in range(len(heights)):
            pacifics.add((i, 0))

        # cells starting from atlantic ocean
        atlantics = set()
        for i in range(len(heights[0])):
            atlantics.add((len(heights) - 1, i))
        for i in range(len(heights)):
            atlantics.add((i, len(heights[0]) - 1))
        
        pacific_flowables = bfs(pacifics)
        atlantic_flowables = bfs(atlantics)

        # return the union of the set (cells that flow to both oceans)
        return list(pacific_flowables & atlantic_flowables)
        