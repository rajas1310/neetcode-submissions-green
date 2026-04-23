"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key=lambda x:x.start)

        for i in range(len(intervals)-1):
            i1 = intervals[i]
            i2 = intervals[i+1]
            if i1.end > i2.start:
                return False
        return True