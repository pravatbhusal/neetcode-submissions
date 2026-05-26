"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

"""
Intervals questions can be solved by sorting the intervals and dealing with the
problem's constranits from there.

Sort intervals and check for conflicting time between the prev internal and
the current interval.
"""
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        s_intervals = sorted(intervals, key=lambda intv: intv.start)
        for i in range(1, len(s_intervals)):
            cur = s_intervals[i]
            prev = s_intervals[i - 1]
            if cur.start < prev.end:
                return False
        return True