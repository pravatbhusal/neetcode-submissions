"""
Similar Problem: "Merge Intervals"

Sort the intervals to put the overlapping intervals adjacent to each other.

Greedily scan and when two intervals overlap, remove the one that ends later
(keeping the smaller end minimizes future conflicts). Count removals until
no overlaps remain.

There are two cases:
1. No overlap: curInterval starts at or after lastInterval ends, advance lastInterval
2. Overlap: remove the interval that ends later, keeping the smaller end to minimize future conflicts
"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort intervals to put overlaps adjacent to each other
        s_intervals = sorted(intervals, key=lambda intv : intv[0])

        lastInterval = s_intervals[0]
        result = 0
        for i in range(1, len(s_intervals)):
            curInterval = s_intervals[i]
            if curInterval[0] >= lastInterval[1]:
                # curInterval is after lastInteral
                lastInterval = curInterval
            else:
                # minimize lastInterval smaller end, keep looping to catch further merges
                result += 1
                lastInterval = [lastInterval[0], min(lastInterval[1], curInterval[1])]

        return result