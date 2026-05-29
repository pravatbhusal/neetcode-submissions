"""
Similar Problem: "Insert Interval"

Sort the intervals to put the overlapping intervals adjacent to each other.

Then, merge adjacent intervals, similar to the "Insert Interval" solution.
In this case, the last element in the result list will continously be
updated if curInterval is an overlapping interval.

There are two cases to merge intervals:
1. After curInterval, where curInterval is immediately before lastInterval 
2. Merge (override), where two intervals overlap with lastInterval
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals to put overlaps adjacent to each other
        s_intervals = sorted(intervals, key=lambda intv : intv[0])

        # initialize result
        result = []
        result.append(s_intervals[0])

        for i in range(1, len(s_intervals)):
            lastInterval = result[-1]
            curInterval = s_intervals[i]
            if curInterval[0] > lastInterval[1]:
                # curInterval is after lastInteral
                result.append(curInterval)
            else:
                # expand lastInterval to absorb curInterval, keep looping to catch further merges
                lastInterval = [lastInterval[0], max(lastInterval[1], curInterval[1])]
                result.pop()
                result.append(lastInterval)

        return result