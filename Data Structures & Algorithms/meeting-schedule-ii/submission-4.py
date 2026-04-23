"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        rooms = 0
        intervals = sorted(intervals, key= lambda x: x.start)

        slots = intervals

        while slots:
            rooms += 1
            remaining_slots = []
            last_end = -1

            for i in range(len(slots)):
                i1 = slots[i]

                if last_end > i1.start:
                    remaining_slots.append(i1)
                else:
                    last_end = i1.end
            
            slots = remaining_slots
        
        return rooms