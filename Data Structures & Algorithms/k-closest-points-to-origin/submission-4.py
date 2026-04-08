class Solution:
    """
    Solution:
    1. Calculate the distance to (0,0) for all points
    2. Add each distance value to a min heap.
    3. Pop k times from the min heap to find the k smallest
    distances to the origin.
    """
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # add all distances into a dictionary of distance -> list of points
        distance_dict = defaultdict(list)
        for point in points:
            distance = math.sqrt((point[0] - 0) ** 2 + (point[1] - 0) ** 2)
            distance_dict[distance].append(point)

        # add the distances into a min heap
        distances = list(distance_dict.keys())
        heapq.heapify(distances)
        result = []

        # keep popping from min heap till we get k results
        while len(result) < k:
            distance = heapq.heappop(distances)
            points = distance_dict[distance]
            for point in points:
                if len(result) < k:
                    result.append(point)
        
        return result