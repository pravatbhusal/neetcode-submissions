"""
Brute-force O(N * M): For each query, check if it's in range of each interval.
Append the interval where the query is in range and has the smallest length.

Sorting (WRONG): Sort the intervals by length (using custom comparator).
For each query, binary search the sorted intervals to find the smallest interval.

Sorting O(NLog(N) + MLog(M)): Sort the intervals by start time and sort the queries.
For each sorted query, if the query is in range of the next interval, then add
that interval's length to min heap. Set the query's min length to the top of the
min heap.
"""
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        s_queries = sorted(queries)

        min_heap = []
        result = dict()
        i = 0
        for q in s_queries:
            while i < len(intervals) and intervals[i][0] <= q:
                # query is in range of interval
                start, end = intervals[i]
                heapq.heappush(min_heap, (end - start + 1, end))
                i += 1
            # pop intervals from heap out of the query's range
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            # set query's min length (top of min heap)
            result[q] = min_heap[0][0] if min_heap else -1
        
        return [result[q] for q in queries]