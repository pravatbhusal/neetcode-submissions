"""
Intervals list is already sorted, so we can use binary search to find where to insert newInterval.
Binary search is O(log(N)) time, but the overall complexity will still be O(N).

Overally complexity is O(N) because we need to insert or remove from the middle of the list to put newInterval.
Therefore, we can simply linear search the list if overall complexity is O(N).

There are three cases to put newInterval:
1. Before curInterval, where curInterval is immediately after newInterval
2. After curInterval, where curInterval is immediately before newInterval 
3. Merge (override), where two intervals overlap with newInterval
"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for i in range(len(intervals)):
            curInterval = intervals[i]
            if curInterval[1] < newInterval[0]:
                # curInterval is before newInterval
                result.append(curInterval)
            elif curInterval[0] > newInterval[1]:
                # curInterval is after newInterval
                result.append(newInterval)
                return result + intervals[i:]
            else:
                # override newInterval to merge with the two colliding intervals
                # loop adds the overwritten newInterval in next iteration
                newInterval = [min(newInterval[0], curInterval[0]), max(newInterval[1], curInterval[1])]
        
        # edge case, newInterval belongs at the end
        result.append(newInterval)
        return result