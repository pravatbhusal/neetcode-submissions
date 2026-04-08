class Solution:
    """
    Solution:
    1. Calculate the distance to (0,0) for all points
    2. Add each distance value to a min heap.
    3. Pop k times from the min heap to find the k smallest
    distances to the origin.
    """
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # add all distances into a tuple list of (distance, point)
        distances = []
        for point in points:
            distance = math.sqrt((point[0] - 0) ** 2 + (point[1] - 0) ** 2)
            distances.append((distance, point))

        # put the distances into a min heap
        # tuple comparator uses 0th element (distance)
        heapq.heapify(distances)

        # keep popping from min heap till we get k results
        result = []
        while len(result) < k:
            distance = heapq.heappop(distances)
            point = distance[1]
            result.append(point)
        
        return result