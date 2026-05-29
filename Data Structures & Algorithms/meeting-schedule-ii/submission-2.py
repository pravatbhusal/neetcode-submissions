"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

"""
Similar Problem: "Merge Intervals"

In Merge Intervals you combine overlapping intervals and count the merged groups.
Here it's the opposite — you want to count how many intervals are simultaneously
active at "max" overlap.

Sort the intervals to put the overlapping intervals adjacent to each other.

There are two cases to find min number of rooms:
1. No overlap: curInterval has no conflicts and no new room is needed
2. Overlap: When two intervals overlap with lastInterval, need a new room

This can be solved using two ptrs: start_ptr and end_ptr.
Create two sorted arrays of the start and end times for each meeting.
One ptr will track the start time, another ptr will track the end time.

"""
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        start_times = sorted(intv.start for intv in intervals)
        end_times = sorted(intv.end for intv in intervals)

        rooms = 0
        end_ptr = 0

        for start_ptr in range(len(start_times)):
            if start_times[start_ptr] >= end_times[end_ptr]:
                # no overlap: a room freed up, reuse it
                end_ptr += 1
            else:
                # overlap: new meeting starts before earliest ending, need a new room
                rooms += 1

        return rooms