"""
Similar Problem: "Merge Intervals"

Sort the intervals to put the overlapping intervals adjacent to each other.

We can greedily find out if we need to keep removing an interval to not make
it overlap. From the start of an overlap, keep track of lastInterval[1] and
keep counting curInterval up till curInterval[0] no longer overlaps.
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
            elif curInterval[0] < lastInterval[1]:
                # overlap, keep looping to catch further merges
                result += 1
                lastInterval = [lastInterval[0], min(lastInterval[1], curInterval[1])]

        return result