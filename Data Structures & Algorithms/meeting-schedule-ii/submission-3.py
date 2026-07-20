"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        currrooms = maxrooms = 0
        s = e = 0
        while s<len(intervals):
            if start[s]<end[e]:
                currrooms += 1
                s+=1
            else:
                currrooms -= 1
                e += 1
            maxrooms = max(maxrooms, currrooms)
        return maxrooms