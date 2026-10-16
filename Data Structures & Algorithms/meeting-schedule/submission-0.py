"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        intervals.sort(key=lambda x: x.start)

        # if a meeting start before another ending => conflict

        for i in range(1, len(intervals)):

            prevEnd = intervals[i-1].end
            nextStart = intervals[i].start

            if nextStart < prevEnd:
                return False
        
        return True



