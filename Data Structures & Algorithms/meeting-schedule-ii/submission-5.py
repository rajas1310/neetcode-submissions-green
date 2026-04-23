"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        num_rooms = defaultdict(int)
        for i in intervals:
            num_rooms[i.start] += 1
            num_rooms[i.end] -= 1
        print(num_rooms)
        prev, res = 0,0
        for i in sorted(num_rooms.keys()):
            prev += num_rooms[i]
            res = max(res, prev)
        return res
