"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0 or len(intervals) == 1:
            return True

        # solution 1: create array of size [0, ... 1 mil]
        # for each interval, fill-in the time. then check conflict

        # solution 2: use comparator and sort
        # iterate sorted list, check if cur intv conflicts with prev intv
        s_intvs = sorted(intervals, key=lambda intv: intv.start)
        for i in range(1, len(s_intvs)):
            prev = s_intvs[i - 1]
            cur = s_intvs[i]
            if cur.start < prev.end or prev.end >= cur.end:
                # prev meeting did not end before cur
                return False
        return True