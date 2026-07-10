"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <2: return True
        intervals.sort(key=lambda x: x.end)
        for i in range(len(intervals)):
            curr = intervals[i]
            if i+1<len(intervals) and curr.end>intervals[i+1].start:
                return False
        return True
            
